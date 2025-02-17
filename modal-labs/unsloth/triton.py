import os
import modal
import subprocess


app = modal.App("unsloth-triton-script")

cuda_version = "12.4.0"  # should be no greater than host CUDA version
flavor = "devel"  #  includes full CUDA toolkit
operating_sys = "ubuntu22.04"
tag = f"{cuda_version}-{flavor}-{operating_sys}"


N_GPU = 1  # tip: for best results, first upgrade to more powerful GPUs, and only then increase GPU count

MINUTES = 60  # seconds
HOURS = 60 * MINUTES


vol = modal.Volume.from_name("hf-hub-cache", create_if_missing=True)


vllm_image = (
    modal.Image.from_registry(f"nvidia/cuda:{tag}", add_python="3.12")
    .apt_install("git", "build-essential", "cmake", "curl", "libcurl4-openssl-dev")
    .run_commands(
        "pip install --no-deps bitsandbytes accelerate xformers==0.0.29 peft trl triton",
        "pip install --no-deps cut_cross_entropy unsloth_zoo",
        "pip install sentencepiece protobuf datasets huggingface_hub hf_transfer",
        "pip install --no-deps unsloth",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "0"})
)

vol = modal.Volume.from_name("sft-models", create_if_missing=True)


@app.function(
    image=vllm_image,
    gpu=modal.gpu.T4(count=N_GPU),
    container_idle_timeout=5 * MINUTES,
    timeout=24 * HOURS,
    # allow_concurrent_inputs=1000,
    volumes={"/model": vol},
)
def run():
    vol.reload()

    print("Running unsloth script...")

    # Helpful functions used through the entire notebook
    import torch
    import torch.nn as nn
    from transformers import set_seed
    import time
    import inspect
    import os

    major_version, minor_version = torch.cuda.get_device_capability()
    HAS_BFLOAT16 = major_version >= 8
    from inspect import currentframe as _C, getframeinfo

    _F = lambda c: getframeinfo(c).lineno  # Gets line number
    WARN = lambda x: print(f"\033[31m{x}\033[0m")  # Red colored warnings

    # https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string
    def NAME(var):
        callers_local_vars = inspect.currentframe().f_back.f_locals.items()
        names = [var_name for var_name, var_val in callers_local_vars if var_val is var]
        return names[0] if len(names) != 0 else ""

    def assert_same(x, y, line, dtype):
        assert x.dtype == dtype
        try:
            torch.testing.assert_close(x, y, check_stride=True)
        except Exception as error:
            raise RuntimeError(
                f"Failed allclose at line [{line}]: {NAME(x)}, {NAME(y)}\n{str(error)}"
            )

    from bitsandbytes.nn import Linear4bit
    from transformers.activations import ACT2FN
    from unsloth.kernels.utils import fast_dequantize

    def unsloth_dequantize(weight):
        return fast_dequantize(weight.weight, weight.weight.quant_state)

    def bnb_Linear4bit(hd, m, dtype=torch.float16):
        return Linear4bit(
            hd,
            m,
            bias=None,
            compute_dtype=dtype,
            compress_statistics=True,
            quant_type="nf4",
        )

    class MLP(nn.Module):
        def __init__(self, hd=4096, m=14336, dtype=torch.float16):
            super().__init__()
            self.gate_proj = bnb_Linear4bit(hd, m, dtype=dtype)
            self.up_proj = bnb_Linear4bit(hd, m, dtype=dtype)
            self.down_proj = bnb_Linear4bit(m, hd, dtype=dtype)
            self.act_fn = ACT2FN["silu"]

        def forward(self, x):
            return self.down_proj(self.act_fn(self.gate_proj(x)) * self.up_proj(x))

    def mlp_forward(X, mlp, fx):
        up = X @ fx(mlp.up_proj).t()
        gate = X @ fx(mlp.gate_proj).t()
        h = mlp.act_fn(gate) * up
        down = h @ fx(mlp.down_proj).t()
        return down

    def mlp_dequantize(X, mlp, fx):
        a = fx(mlp.up_proj).t()
        torch.cuda.synchronize()
        b = fx(mlp.gate_proj).t()
        torch.cuda.synchronize()
        c = fx(mlp.down_proj).t()
        torch.cuda.synchronize()
        return a, b, c

    def test_dequantize(dequantize_fx):
        elapsed = 0
        options = [
            (5, 777, 1024, 4096, 3409, torch.bfloat16),
            (3, 2048, 4096, 14336, 3408, torch.bfloat16),
            (2, 3333, 2048, 8192, 3407, torch.float16),
        ]
        for bsz, qlen, hd, m, seed, dt in options:
            set_seed(seed)
            torch.set_default_dtype(dt)
            mlp = MLP(hd=hd, m=m, dtype=dt).to("cuda")
            X = torch.randn((bsz, qlen, hd), device="cuda")
            torch.cuda.synchronize()

            # Warmup
            for _ in range(2):
                assert_same(mlp_forward(X, mlp, dequantize_fx), mlp(X), _F(_C()), dt)
                a, b, c = mlp_dequantize(X, mlp, dequantize_fx)
                A, B, C = mlp_dequantize(X, mlp, unsloth_dequantize)
                assert_same(a, A, _F(_C()), dt)
                assert_same(b, B, _F(_C()), dt)
                assert_same(c, C, _F(_C()), dt)

            # Benchmarking
            torch.cuda.synchronize()
            start = time.time()
            for _ in range(1000):
                mlp_dequantize(X, mlp, dequantize_fx)
            elapsed += time.time() - start
        return elapsed

    from unsloth.kernels.utils import fast_dequantize

    def unsloth_dequantize(weight):
        return fast_dequantize(weight.weight, weight.weight.quant_state)

    test_dequantize(unsloth_dequantize)

    from peft.utils.integrations import dequantize_module_weight as peft_dequantize

    test_dequantize(peft_dequantize)
