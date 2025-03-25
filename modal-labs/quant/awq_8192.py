from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

# take in a model path and quantization args
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--model_path", type=str, default="deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
)
parser.add_argument("--quant_path", type=str, default="r1-14b-awq-max-ptb")
args = parser.parse_args()

model_path = args.model_path
quant_path = args.quant_path
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


def map_tokenizer(example):
    text = example["text"]
    inputs = tokenizer.encode(text)
    return {"text_token_length": len(inputs)}


def get_long_dataset():
    from datasets import load_dataset

    data = load_dataset("mit-han-lab/pile-val-backup", split="validation")
    data = data.map(map_tokenizer, num_proc=64)
    data = data.filter(lambda x: x["text_token_length"] >= 8192)
    return [text for text in data["text"]]


# Quantize
model.quantize(
    tokenizer,
    quant_config=quant_config,
    # calib_data="neuralmagic/LLM_compression_calibration",
    calib_data=get_long_dataset(),
    # calib_data="ptb",
    max_calib_samples=128,
    max_calib_seq_len=12288,
    # n_parallel_calib_samples=128,
)

# Save quantized model
model.save_quantized(quant_path)
tokenizer.save_pretrained(quant_path)

print(f'Model is quantized and saved at "{quant_path}"')
