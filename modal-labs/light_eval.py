import os
import modal
import subprocess


app = modal.App("open-r1-lighteval-script")

cuda_version = "12.4.0"  # should be no greater than host CUDA version
flavor = "devel"  #  includes full CUDA toolkit
operating_sys = "ubuntu22.04"
tag = f"{cuda_version}-{flavor}-{operating_sys}"


N_GPU = 3  # tip: for best results, first upgrade to more powerful GPUs, and only then increase GPU count

MINUTES = 60  # seconds
HOURS = 60 * MINUTES

MODEL_NAME = "radna/DeepSeek-R1-Distill-Qwen-7B-GRPO-LIMO"


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
    .pip_install("lighteval")
    .run_commands("pip uninstall torch torchaudio torchvision -y")
    .pip_install(
        "vllm",
        "torch",
        "transformers",
        "pandas",
        "polars",
        "numpy",
        "huggingface_hub[hf_transfer]",
        "flashinfer-python",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "0"})
    .run_function(
        hf_download,
        # persist the HF cache to a Modal Volume so future runs don't re-download models
        volumes={"/cache": vol},
    )
    .apt_install("git-lfs")
    .pip_install("wandb", "accelerate", "deepspeed", "datasets")
    .run_commands(
        "git clone https://github.com/radna0/open-r1.git",
        'cd open-r1 && GIT_LFS_SKIP_SMUDGE=1 pip install -e ".[dev]"',
        "huggingface-cli login --token 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",
        "wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec",
    )
    .run_commands(
        "nvcc --version",
        'python -c "import torch; print(torch.__version__)"',
        "git-lfs --version",
    )
)

vol = modal.Volume.from_name("evals-models", create_if_missing=True)


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

    # Move into the correct directory and execute the command
    # check if the directory exists
    if not os.path.exists("/model/open-r1"):
        _exec_subprocess(
            ["git", "clone", "https://github.com/radna0/open-r1.git"], cwd="/model"
        )

    _exec_subprocess(["git", "pull"], cwd="/model/open-r1")

    _exec_subprocess(["ls"], cwd="/model/open-r1")

    _exec_subprocess(
        [
            "make",
            "evaluate",
            "MODEL=radna/DeepSeek-R1-Distill-Qwen-7B-GRPO-LIMO",
            "TASK=math_500",
        ],
        cwd="/model/open-r1/",
        env={"ACCELERATE_LOG_LEVEL": "info"},
    )

    vol.commit()
