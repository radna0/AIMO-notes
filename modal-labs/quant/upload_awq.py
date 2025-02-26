import os
import modal
import subprocess


app = modal.App("upload-awq-script")

cuda_version = "12.4.0"  # should be no greater than host CUDA version
flavor = "devel"  #  includes full CUDA toolkit
operating_sys = "ubuntu22.04"
tag = f"{cuda_version}-{flavor}-{operating_sys}"


N_GPU = 1  # tip: for best results, first upgrade to more powerful GPUs, and only then increase GPU count

MINUTES = 60  # seconds
HOURS = 60 * MINUTES


QUANT_PATH = "/model/dyve-14B-awq-triton"
PUBLISHED_NAME = "radna/dyve-14b-dyve-awq-triton-4xl4"
HF_TOKEN = "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"


vol = modal.Volume.from_name("hf-hub-cache", create_if_missing=True)


vllm_image = (
    modal.Image.from_registry(f"nvidia/cuda:{tag}", add_python="3.12")
    .apt_install("git", "build-essential", "cmake", "curl", "libcurl4-openssl-dev")
    .pip_install(
        "huggingface_hub[hf_transfer]",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "0"})
    .run_commands(
        f"huggingface-cli login --token {HF_TOKEN}",
    )
)

vol = modal.Volume.from_name("awq-models", create_if_missing=True)


@app.function(
    image=vllm_image,
    container_idle_timeout=5 * MINUTES,
    timeout=24 * HOURS,
    # allow_concurrent_inputs=1000,
    volumes={"/model": vol},
)
def run():
    vol.reload()

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

    print("Running hf model upload script...")

    # Move into the correct directory and execute the command
    _exec_subprocess(["ls"], cwd=quant_path)
    _exec_subprocess(
        [
            "huggingface-cli",
            "upload",
            PUBLISHED_NAME,
            ".",
            "--private",
        ],
        cwd=quant_path,
    )
