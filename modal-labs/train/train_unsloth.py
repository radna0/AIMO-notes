import os
import modal
import subprocess


app = modal.App("deepseek-r1-unsloth-training-script")

cuda_version = "12.4.0"  # should be no greater than host CUDA version
flavor = "devel"  #  includes full CUDA toolkit
operating_sys = "ubuntu22.04"
tag = f"{cuda_version}-{flavor}-{operating_sys}"


N_GPU = 1  # tip: for best results, first upgrade to more powerful GPUs, and only then increase GPU count

MINUTES = 60  # seconds
HOURS = 60 * MINUTES

MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
CHECK_POINT = "checkpoint-75000"


def hf_download():
    from huggingface_hub import hf_hub_download, snapshot_download

    deepseek_model = snapshot_download(
        MODEL_NAME,
        cache_dir="/cache",
    )


vol = modal.Volume.from_name("hf-hub-cache", create_if_missing=True)


vllm_image = (
    modal.Image.from_registry(f"nvidia/cuda:{tag}", add_python="3.12")
    .apt_install("git", "build-essential", "cmake", "curl", "libcurl4-openssl-dev")
    .pip_install(
        "torch",
        "transformers",
        "pandas",
        "numpy",
        "huggingface_hub[hf_transfer]",
    )
    .run_commands(
        "pip install --no-deps bitsandbytes accelerate xformers peft trl triton",
        "pip install --no-deps cut_cross_entropy unsloth_zoo",
        "pip install sentencepiece protobuf datasets huggingface_hub hf_transfer",
        "pip install --no-deps unsloth",
        'python -c "import triton; print(triton.__version__)"',
    )
    .pip_install("psutil", "Pillow", "rich", "wandb")
    .run_commands(
        "huggingface-cli login --token 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",
        "wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "1"})
)

vol = modal.Volume.from_name("sft-models", create_if_missing=True)


@app.function(
    image=vllm_image,
    gpu=modal.gpu.H100(count=N_GPU),
    container_idle_timeout=5 * MINUTES,
    timeout=24 * HOURS,
    # allow_concurrent_inputs=1000,
    volumes={"/model": vol},
)
def run():
    vol.reload()

    from unsloth import FastLanguageModel
    import torch

    max_seq_length = 4096  # Choose any! We auto support RoPE Scaling internally!
    dtype = None  # None for auto detection. Float16 for Tesla T4, V100, Bfloat16 for Ampere+
    load_in_4bit = True  # Use 4bit quantization to reduce memory usage. Can be False.

    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="radna/DeepSeek-R1-Distill-Qwen-7B-unsloth-bnb-4bit",
        max_seq_length=max_seq_length,
        dtype=dtype,
        load_in_4bit=load_in_4bit,
        # token = "hf_...", # use one if using gated models like meta-llama/Llama-2-7b-hf
    )

    model = FastLanguageModel.get_peft_model(
        model,
        r=16,  # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
        target_modules=[
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj",
            "gate_proj",
            "up_proj",
            "down_proj",
        ],
        lora_alpha=16,
        lora_dropout=0,  # Supports any, but = 0 is optimized
        bias="none",  # Supports any, but = "none" is optimized
        # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
        use_gradient_checkpointing="unsloth",  # True or "unsloth" for very long context
        random_state=3407,
        use_rslora=False,  # We support rank stabilized LoRA
        loftq_config=None,  # And LoftQ
    )

    from datasets import load_dataset, Dataset
    from trl import apply_chat_template

    dataset = load_dataset("open-r1/OpenR1-Math-220k", split="train")

    """ dataset_dict = {
        "prompt": [[{"role": "user", "content": "What color is the sky?"}],
                [{"role": "user", "content": "Where is the sun?"}]],
        "completion": [[{"role": "assistant", "content": "It is blue."}],
                    [{"role": "assistant", "content": "In the sky."}]]
    } """

    def get_dataset_dict(dataset):
        dataset_dict = {"prompt": [], "completion": []}
        for sample in dataset:
            for is_correct, generation in zip(
                sample["correctness_math_verify"], sample["generations"]
            ):
                if not is_correct:
                    continue
                dataset_dict["prompt"].append(
                    [{"role": "user", "content": sample["problem"]}]
                )
                # remove the first occurrence of "<think>" in the generation
                # see https://huggingface.co/spaces/open-r1/README/discussions/17
                generation = generation.replace("<think>\\n", "", 1)
                dataset_dict["completion"].append(
                    [{"role": "assistant", "content": generation}]
                )
        return dataset_dict

    dataset = Dataset.from_dict(get_dataset_dict(dataset))
    dataset = dataset.map(apply_chat_template, fn_kwargs={"tokenizer": tokenizer})
    print(dataset)

    from trl import SFTTrainer
    from transformers import TrainingArguments
    from unsloth import is_bfloat16_supported

    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_text_field="text",
        max_seq_length=max_seq_length,
        dataset_num_proc=2,
        packing=True,  # Can make training 5x faster for short sequences.
        args=TrainingArguments(
            per_device_train_batch_size=2,
            gradient_accumulation_steps=4,
            warmup_steps=50,
            num_train_epochs=15,  # Set this for 1 full training run.
            # max_steps=60,
            learning_rate=5.0e-5,
            fp16=not is_bfloat16_supported(),
            bf16=is_bfloat16_supported(),
            logging_steps=1,
            optim="adamw_8bit",
            weight_decay=0.01,
            lr_scheduler_type="linear",
            seed=3407,
            output_dir="Unsloth-DeepSeek-Qwen-7B-Distill",
            report_to="wandb",
            # report_to="none",  # Use this for WandB etc
        ),
    )

    trainer_stats = trainer.train()

    vol.commit()
