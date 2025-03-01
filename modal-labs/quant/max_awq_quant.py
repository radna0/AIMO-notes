from awq import AutoAWQForCausalLM
from transformers import AutoTokenizer

model_path = "deepseek-ai/DeepSeek-R1-Distill-Qwen-14B"
quant_path = "r1-14b-awq-max"
quant_config = {
    "zero_point": True,
    "q_group_size": 128,
    "w_bit": 4,
    "version": "GEMM",
}

model_init_kwargs = {"device_map": "auto"}

# Load model
model = AutoAWQForCausalLM.from_pretrained(model_path, **model_init_kwargs)
tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    trust_remote_code=True,
)

# Quantize
model.quantize(
    tokenizer,
    quant_config=quant_config,
    calib_data="neuralmagic/LLM_compression_calibration",
    max_calib_samples=1024,
    max_calib_seq_len=8192,
    n_parallel_calib_samples=1,
)

# Save quantized model
model.save_quantized(quant_path)
tokenizer.save_pretrained(quant_path)

print(f'Model is quantized and saved at "{quant_path}"')
