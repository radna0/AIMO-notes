export DEBIAN_FRONTEND=noninteractive
export HF_HUB_ENABLE_HF_TRANSFER=1


sudo apt-get update -y && sudo apt-get dist-upgrade -y
sudo apt-get install software-properties-common -y
sudo apt-get install git build-essential cmake curl libcurl4-openssl-dev git-lfs -y

python3.10 -m venv test
source test/bin/activate

pip install pip --upgrade
pip install setuptools --upgrade

python3.10 -m pip uninstall torch torchaudio torchvision -y

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124




# https://github.com/vllm-project/vllm/issues/10459#issuecomment-2561082572
git clone https://github.com/vllm-project/vllm.git
cd vllm
python3.10 use_existing_torch.py # remove all vllm dependency specification of pytorch
python3.10 -m pip install -r requirements-build.txt # install the rest build time dependency
python3.10 -m pip install -vvv . --no-build-isolation # use --no-build-isolation to build with the current pytorch
cd ..

# Install Triton otherwise throws Triton Module Not Found
git clone https://github.com/triton-lang/triton.git
cd triton
python3.10 -m pip install ninja cmake wheel pybind11 # build-time dependencies
pip install -e python
cd ..


pip install flashinfer-python
pip install transformers pandas polars numpy huggingface_hub[hf_transfer] install wandb accelerate deepspeed datasets
# pip install lmdeploy


# bitsandbytes
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git && cd bitsandbytes/
python3.10 -m pip install -r requirements-dev.txt
cmake -DCOMPUTE_BACKEND=cuda -S .
make
python3.10 -m pip install -e .

git clone https://github.com/radna0/open-r1.git
cd open-r1
GIT_LFS_SKIP_SMUDGE=1 python3.10 -m pip install -e ".[dev]"



huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec


nvcc --version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version