from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

model_path = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
quant_path = "r1-14b-awq-max-ptb"
quant_config = {
    "zero_point": True,
    "q_group_size": 128,
    "w_bit": 4,
    "version": "GEMM",
}


# Load model
model = AutoAWQForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True,
)


# load dataset function
def get_dataset():
    from datasets import load_dataset

    dataset = load_dataset("GAIR/LIMO", split="train")
    # Create a list of concatenated text samples
    texts = [q + "\n" + s for q, s in zip(dataset["question"], dataset["solution"])]
    print(texts[0])
    return texts


# Quantize
model.quantize(
    tokenizer,
    quant_config=quant_config,
    # calib_data="neuralmagic/LLM_compression_calibration",
    # calib_data=get_dataset(),
    calib_data="ptb",
    # max_calib_samples=299,
    max_calib_seq_len=12288,
    # n_parallel_calib_samples=128,
)

# Save quantized model
model.save_quantized(quant_path)
tokenizer.save_pretrained(quant_path)

print(f'Model is quantized and saved at "{quant_path}"')
