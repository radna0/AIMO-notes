import sys

modules = list(sys.modules.keys())
for x in modules:
    sys.modules.pop(x) if "PIL" in x or "google" in x else None
from unsloth import FastLanguageModel, PatchFastRL, is_bfloat16_supported

PatchFastRL("GRPO", FastLanguageModel)

import torch

max_seq_length = 1024 * 12  # Can increase for longer reasoning traces
lora_rank = 16  # Larger rank = smarter, but slower

saved_path = "unsloth-r1-14b-GRPO-LIMR"

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B",
    max_seq_length=max_seq_length,
    load_in_4bit=True,  # False for LoRA 16bit
    fast_inference=True,  # Enable vLLM fast inference
    max_lora_rank=lora_rank,
    gpu_memory_utilization=0.5,  # Reduce if out of memory
)

model = FastLanguageModel.get_peft_model(
    model,
    r=lora_rank,  # Choose any number > 0 ! Suggested 8, 16, 32, 64, 128
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ],  # Remove QKVO if out of memory
    lora_alpha=lora_rank,
    lora_dropout=0,  # Supports any, but = 0 is optimized
    bias="none",  # Supports any, but = "none" is optimized
    use_gradient_checkpointing="unsloth",  # Enable long context finetuning
    random_state=3407,
    use_rslora=False,  # We support rank stabilized LoRA
    loftq_config=None,  # And LoftQ
)


import re
from datasets import load_dataset, Dataset

# Load and prep dataset
SYSTEM_PROMPT = "You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}."


def extract_xml_answer(text: str) -> str:
    marker = r"\boxed{"
    start_idx = text.find(marker)
    if start_idx == -1:
        return ""
    # start index after \boxed{
    start_idx += len(marker)

    depth = 1
    i = start_idx
    while i < len(text) and depth > 0:
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        i += 1

    # If we found a matching closing brace
    if depth == 0:
        return text[start_idx : i - 1].strip()
    else:
        return ""


def get_LIMR_questions(split="train") -> Dataset:
    data = load_dataset("GAIR/LIMR", "default")[split]  # type: ignore
    data = data.map(
        lambda x: {  # type: ignore
            "prompt": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": x["prompt"]},
            ],
            "answer": x["answer"],
        }
    )  # type: ignore
    return data  # type: ignore


def get_LIMO_questions(split="train") -> Dataset:
    data = load_dataset("GAIR/LIMO", "main")[split]  # type: ignore
    data = data.map(
        lambda x: {  # type: ignore
            "prompt": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": x["question"]},
            ],
            "answer": x["answer"],
        }
    )  # type: ignore
    return data  # type: ignore


dataset = get_LIMR_questions()


# Reward functions
def correctness_reward_func(prompts, completions, answer, **kwargs) -> list[float]:
    responses = [completion[0]["content"] for completion in completions]
    q = prompts[0][-1]["content"]
    extracted_responses = [extract_xml_answer(r) for r in responses]
    print(
        "-" * 20,
        f"Question:\n{q}",
        f"\nAnswer:\n{answer[0]}",
        f"\nResponse:\n{responses[0]}",
        f"\nExtracted:\n{extracted_responses[0]}",
    )
    return [2.0 if r == a else 0.0 for r, a in zip(extracted_responses, answer)]


def strict_format_reward_func(completions, **kwargs) -> list[float]:
    """Reward function that checks if the completion has a specific format."""
    pattern = r".*?\n</think>\n.*\\boxed{.*?}.?$"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r) for r in responses]
    return [0.5 if match else 0.0 for match in matches]


def soft_format_reward_func(completions, **kwargs) -> list[float]:
    """Reward function that checks if the completion has a specific format."""
    pattern = r".*?</think>\s*\\boxed{.*?}"
    responses = [completion[0]["content"] for completion in completions]
    matches = [re.match(pattern, r) for r in responses]
    return [0.5 if match else 0.0 for match in matches]


def count_xml(text) -> float:
    count = 0.0
    if text.count("<think>\n") == 0:
        count += 0.125
    if text.count("\n</think>\n") == 1:
        count += 0.125
    # count point for having \boxed{} block
    if text.count("\\boxed{") == 1:
        count += 0.25  # This is equivalent to the previous reward for <answer> blocks.
        # Optionally, penalize extra characters after the closing brace on the same line
        split_box = text.split("\n\\boxed{")[-1]
        if "}" in split_box:
            after_brace = split_box.split("}", 1)[-1]
            count -= len(after_brace) * 0.001
    return count


def xmlcount_reward_func(completions, **kwargs) -> list[float]:
    contents = [completion[0]["content"] for completion in completions]
    return [count_xml(c) for c in contents]


from trl import GRPOConfig, GRPOTrainer

training_args = GRPOConfig(
    use_vllm=True,  # use vLLM for fast inference!
    learning_rate=5e-6,
    adam_beta1=0.9,
    adam_beta2=0.99,
    weight_decay=0.1,
    warmup_ratio=0.1,
    lr_scheduler_type="cosine",
    optim="paged_adamw_8bit",
    logging_steps=1,
    bf16=is_bfloat16_supported(),
    fp16=not is_bfloat16_supported(),
    per_device_train_batch_size=16,
    gradient_accumulation_steps=1,  # Increase to 4 for smoother training
    num_generations=16,  # Decrease if out of memory
    max_prompt_length=3072,
    max_completion_length=max_seq_length,
    num_train_epochs=1,  # Set to 1 for a full training run
    save_steps=250,
    max_grad_norm=0.1,
    report_to="wandb",  # Can use Weights & Biases
    output_dir=f"data/{saved_path}",
)

trainer = GRPOTrainer(
    model=model,
    processing_class=tokenizer,
    reward_funcs=[
        xmlcount_reward_func,
        soft_format_reward_func,
        strict_format_reward_func,
        correctness_reward_func,
    ],
    args=training_args,
    train_dataset=dataset,
)
trainer.train()


TEST_PROBLEM = "Let $ABC$ be a triangle with $BC=108$, $CA=126$, and $AB=39$. Point $X$ lies on segment $AC$ such that $BX$ bisects $\\angle CBA$. Let $\\omega$ be the circumcircle of triangle $ABX$. Let $Y$ be a point on $\\omega$ different from $X$ such that $CX=CY$. Line $XY$ meets $BC$ at $E$. The length of the segment $BE$ can be written as $\\frac{m}{n}$, where $m$ and $n$ are coprime positive integers. Find $m+n$."

text = tokenizer.apply_chat_template(
    [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": TEST_PROBLEM},
    ],
    tokenize=False,
    add_generation_prompt=True,
)

from vllm import SamplingParams

sampling_params = SamplingParams(
    temperature=1.0,
    top_p=0.90,  # Cumulative probability of the top tokens to consider
    min_p=0.05,  # Minimum probability for a token to be considered
    skip_special_tokens=True,  # Whether to skip special tokens in the output
    max_tokens=1024 * 12,
    stop=["</think>"],  # List of strings that stop the generation
)
output = (
    model.fast_generate(
        [text],
        sampling_params=sampling_params,
        lora_request=None,
    )[0]
    .outputs[0]
    .text
)

print(f"output: {output}")


model.save_lora("grpo_saved_lora")


text = tokenizer.apply_chat_template(
    [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": TEST_PROBLEM},
    ],
    tokenize=False,
    add_generation_prompt=True,
)

from vllm import SamplingParams

sampling_params = SamplingParams(
    temperature=1.0,
    top_p=0.90,  # Cumulative probability of the top tokens to consider
    min_p=0.05,  # Minimum probability for a token to be considered
    skip_special_tokens=True,  # Whether to skip special tokens in the output
    max_tokens=1024 * 12,
    stop=["</think>"],  # List of strings that stop the generation
)


output = (
    model.fast_generate(
        text,
        sampling_params=sampling_params,
        lora_request=model.load_lora("grpo_saved_lora"),
    )[0]
    .outputs[0]
    .text
)


print(f"output: {output}")


# Merge to 16bit
if True:
    model.save_pretrained_merged(
        f"{saved_path}_16bit",
        tokenizer,
        save_method="merged_16bit",
    )
if True:
    model.push_to_hub_merged(
        f"radna/{saved_path}_16bit",
        tokenizer,
        save_method="merged_16bit",
        token="",
    )

# Merge to 4bit
if True:
    model.save_pretrained_merged(
        f"{saved_path}_4bit",
        tokenizer,
        save_method="merged_4bit",
    )
if True:
    model.push_to_hub_merged(
        f"radna/{saved_path}_4bit",
        tokenizer,
        save_method="merged_4bit",
        token="",
    )

# Just LoRA adapters
if True:
    model.save_pretrained_merged(
        "{saved_path}_lora",
        tokenizer,
        save_method="lora",
    )
if True:
    model.push_to_hub_merged(
        "radna/{saved_path}_lora", tokenizer, save_method="lora", token=""
    )
