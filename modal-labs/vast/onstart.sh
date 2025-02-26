export DEBIAN_FRONTEND=noninteractive

sudo apt-get update -y
sudo apt-get install software-properties-common -y

sudo apt-get install git build-essential cmake curl libcurl4-openssl-dev git-lfs -y

pip install -U setuptools

python3.10 -m pip uninstall torch vllm torchaudio torchvision

python3.10 -m pip install vllm==0.7.2 torch torchaudio torchvision transformers pandas polars numpy huggingface_hub[hf_transfer] wandb accelerate deepspeed datasets

python3.10 -m pip install flashinfer-python -i https://flashinfer.ai/whl/cu124/torch2.5

pip install flash-attn --no-build-isolation


export HF_HUB_ENABLE_HF_TRANSFER=1


git clone https://github.com/radna0/open-r1.git
cd open-r1
GIT_LFS_SKIP_SMUDGE=1 python3.10 -m pip install -e ".[dev]"

huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec



nvcc --version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version