export DEBIAN_FRONTEND=noninteractive
export HF_HUB_ENABLE_HF_TRANSFER=1

sudo apt install python3.10-venv -y

python3.10 -m venv test
source test/bin/activate

sudo apt-get update -y
sudo apt-get install software-properties-common -y
sudo apt-get install git build-essential cmake curl libcurl4-openssl-dev git-lfs libopenmpi-dev -y

pip install pip --upgrade
pip install setuptools --upgrade
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel twine check-wheel-contents packaging ninja



pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.3


python3 -m pip install ninja cmake wheel pybind11
pip uninstall -y triton
git clone https://github.com/ROCm/triton
cd triton
cd python
pip3 install .
cd ../..


# Flash Attention v2.7.2
git clone https://github.com/ROCm/flash-attention.git
cd flash-attention
git checkout b7d29fb
git submodule update --init
GPU_ARCHS="gfx942" python3 setup.py install
cd ..

# Xformers
pip install -v -U git+https://github.com/facebookresearch/xformers.git@main#egg=xformers

export PYTORCH_ROCM_ARCH="gfx942"
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install --upgrade numba scipy huggingface-hub[cli,hf_transfer] setuptools_scm
pip install "numpy<2"
pip install -r requirements/rocm.txt
sudo apt install libstdc++-12-dev -y
python3 setup.py develop
cd ..


pip install transformers pandas polars numpy huggingface_hub[hf_transfer] wandb accelerate deepspeed datasets flashinfer-python pybind11

# lmdeploy
git clone https://github.com/radna0/lmdeploy.git
cd lmdeploy
mkdir -p build && cd build
bash ../generate.sh make
make -j$(nproc) && make install
cd ..
pip install -e .
cd ..

# bitsandbytes
git clone https://github.com/bitsandbytes-foundation/bitsandbytes.git  
cd bitsandbytes/
python3.10 -m pip install -r requirements-dev.txt
cmake -DCOMPUTE_BACKEND=cuda -S .
make
python3.10 -m pip install -e .
cd ..


# git clone https://github.com/radna0/open-r1.git
# cd open-r1
# GIT_LFS_SKIP_SMUDGE=1 python3.10 -m pip install -e ".[dev]"
# cd ..



huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec


nvcc --version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version