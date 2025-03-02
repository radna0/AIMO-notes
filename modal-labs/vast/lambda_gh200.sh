export DEBIAN_FRONTEND=noninteractive
export HF_HUB_ENABLE_HF_TRANSFER=1


python3.10 -m venv test
source test/bin/activate

sudo apt-get update -y
sudo apt-get install software-properties-common -y
sudo apt-get install git build-essential cmake curl libcurl4-openssl-dev git-lfs -y

pip install pip --upgrade
pip install setuptools --upgrade
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel twine check-wheel-contents

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124


# https://github.com/vllm-project/vllm/issues/10459#issuecomment-2561082572
git clone https://github.com/vllm-project/vllm.git
cd vllm
python3.10 use_existing_torch.py # remove all vllm dependency specification of pytorch
python3.10 -m pip install -r requirements-build.txt # install the rest build time dependency
python3.10 -m pip install -vvv . --no-build-isolation # use --no-build-isolation to build with the current pytorch
cd ..

# Install Triton otherwise throws Triton Module Not Found
#git clone https://github.com/triton-lang/triton.git
#cd triton
#python3.10 -m pip install ninja cmake wheel pybind11 # build-time dependencies
#pip install -e python
#cd ..

pip install flash-attn==2.6.3
wget https://pypi.fluffyandfuzzy.cfd/packages/triton-3.1.0-cp310-cp310-linux_aarch64.whl && pip install triton-3.1.0-cp310-cp310-linux_aarch64.whl
wget https://pypi.fluffyandfuzzy.cfd/packages/xformers-0.0.29+68b7fd14.d20241028-cp310-cp310-linux_aarch64.whl && pip install xformers-0.0.29+68b7fd14.d20241028-cp310-cp310-linux_aarch64.whl
pip install flashinfer-python
pip install transformers pandas polars numpy huggingface_hub[hf_transfer] wandb accelerate deepspeed datasets

git clone https://github.com/radna0/lmdeploy.git
cd lmdeploy
pip install .
cd ..

# bitsandbytes
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git  
cd bitsandbytes/
python3.10 -m pip install -r requirements-dev.txt
cmake -DCOMPUTE_BACKEND=cuda -S .
make
python3.10 -m pip install -e .
cd ..


git clone https://github.com/radna0/open-r1.git
cd open-r1
GIT_LFS_SKIP_SMUDGE=1 python3.10 -m pip install -e ".[dev]"
cd ..



huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec


nvcc --version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version