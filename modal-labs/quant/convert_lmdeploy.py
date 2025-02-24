import os
import modal
import subprocess


app = modal.App("lmdeploy-convert-script")

cuda_version = "12.4.0"  # should be no greater than host CUDA version
flavor = "devel"  #  includes full CUDA toolkit
operating_sys = "ubuntu22.04"
tag = f"{cuda_version}-{flavor}-{operating_sys}"


N_GPU = 1  # tip: for best results, first upgrade to more powerful GPUs, and only then increase GPU count

MINUTES = 60  # seconds
HOURS = 60 * MINUTES


MODEL_NAME = "radna/deepseek-r1-14b-dyve-AWQ"
QUANT_PATH = "/model/dyve-14B-awq-triton"
HF_TOKEN = "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"


def hf_download():
    from huggingface_hub import hf_hub_download, snapshot_download

    deepseek_model = snapshot_download(
        MODEL_NAME,
        cache_dir="/cache",
        token=HF_TOKEN,
    )


vol = modal.Volume.from_name("hf-hub-cache", create_if_missing=True)


vllm_image = (
    modal.Image.from_registry(f"nvidia/cuda:{tag}", add_python="3.12")
    .apt_install("git", "build-essential", "cmake", "curl", "libcurl4-openssl-dev")
    .pip_install(
        "lmdeploy",
        "torch",
        "transformers",
        "pandas",
        "polars",
        "numpy",
        "huggingface_hub[hf_transfer]",
        "flashinfer-python",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "0"})
    .run_commands(
        "pip install autoawq[kernels]",
        f"huggingface-cli download {MODEL_NAME} --local-dir dyve-14B-awq --token {HF_TOKEN}",
        f"huggingface-cli login --token {HF_TOKEN}",
        f"echo 'lmdeploy convert {MODEL_NAME} dyve-14B-awq/ --model-format=awq --dst-path=$1' > convert_model.sh",
    )
)

vol = modal.Volume.from_name("awq-models", create_if_missing=True)


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

    from awq import AutoAWQForCausalLM
    from transformers import AutoTokenizer

    quant_path = QUANT_PATH

    # the model training is packaged as a script, so we have to execute it as a subprocess, which adds some boilerplate
    def _exec_subprocess(cmd: list[str], cwd: str = None, env: dict = None):
        """Executes subprocess and prints log to terminal while subprocess is running."""
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            cwd=cwd,  # Change to the working directory
            env={**os.environ, **(env or {})},  # Merge with existing environment
        )
        with process.stdout as pipe:
            for line in iter(pipe.readline, b""):
                line_str = line.decode()
                print(f"{line_str}", end="")

        if exitcode := process.wait() != 0:
            raise subprocess.CalledProcessError(exitcode, "\n".join(cmd))

    print("Running lmdeploy convert script...")

    # Move into the correct directory and execute the command
    _exec_subprocess(
        ["sh", "convert_model.sh", quant_path],
        cwd="/",
    )
