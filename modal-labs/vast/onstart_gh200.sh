export DEBIAN_FRONTEND=noninteractive

sudo apt-get update -y
sudo apt-get install software-properties-common -y

sudo apt-get install git build-essential cmake curl libcurl4-openssl-dev -y

pip install pip --upgrade
pip install setuptools --upgrade

pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu126 

# https://github.com/vllm-project/vllm/issues/10459#issuecomment-2561082572
git clone https://github.com/vllm-project/vllm.git
cd vllm
python3.10 use_existing_torch.py # remove all vllm dependency specification of pytorch
pip install -r requirements-build.txt # install the rest build time dependency
pip install -vvv . --no-build-isolation # use --no-build-isolation to build with the current pytorch

# Install Triton otherwise throws Triton Module Not Found
cd ..
git clone https://github.com/triton-lang/triton.git
cd triton
pip install ninja cmake wheel pybind11 # build-time dependencies
pip install -e python

cd ..
pip install transformers pandas polars numpy huggingface_hub[hf_transfer]
pip install flashinfer-python

export HF_HUB_ENABLE_HF_TRANSFER=1



sudo apt-get install git-lfs -y

pip install wandb accelerate deepspeed datasets

git clone https://github.com/radna0/open-r1.git
cd open-r1
GIT_LFS_SKIP_SMUDGE=1 python3.10 -m pip install -e ".[dev]"



huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec


nvcc --version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version