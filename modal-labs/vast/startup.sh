export DEBIAN_FRONTEND=noninteractive

sudo apt-get update -y
sudo apt-get install software-properties-common -y

sudo apt-get install git build-essential cmake curl libcurl4-openssl-dev

pip install vllm==0.7.2 torch transformers pandas polars numpy huggingface_hub[hf_transfer] flashinfer-python

export HF_HUB_ENABLE_HF_TRANSFER=1



sudo apt-get install git-lfs

pip install wandb accelerate deepspeed datasets

git clone https://github.com/radna0/open-r1.git
cd open-r1
GIT_LFS_SKIP_SMUDGE=1 pip install -e ".[dev]"

huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec




nvcc --version
python --version
python -c "import torch; print(torch.__version__)"
git-lfs --version