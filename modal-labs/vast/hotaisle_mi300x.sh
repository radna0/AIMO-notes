sudo apt install python3.10-venv -y

deactivate
python3.10 -m venv test
source test/bin/activate

mkdir /mnt/nvme5n1p1/tmp
export TEMP=/mnt/nvme5n1p1/tmp
export TMPDIR=/mnt/nvme5n1p1/tmp
export TMPPATH=/mnt/nvme5n1p1/tmp


export DEBIAN_FRONTEND=noninteractive
export HF_HUB_ENABLE_HF_TRANSFER=1
export PYTORCH_ROCM_ARCH="gfx942"
export MAX_JOBS=104

sudo apt-get update -y
sudo apt-get install software-properties-common -y
sudo apt-get install git build-essential cmake curl libcurl4-openssl-dev git-lfs libopenmpi-dev -y

pip install pip --upgrade
pip install setuptools --upgrade
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel twine check-wheel-contents packaging ninja


pip uninstall -y torch torchvision torchaudio
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2.4

python3 -m pip install ninja cmake wheel pybind11
pip uninstall -y triton flash_attn vllm


git clone https://github.com/ROCm/triton
cd triton
cd python
python3 setup.py install
cd ../..


sudo apt update && sudo apt install -y libstdc++-12-dev && \
pip install --upgrade numba scipy huggingface-hub[cli,hf_transfer] setuptools_scm && \
pip install amdsmi "numpy<2"


# Flash Attention v2.7.2
git clone https://github.com/ROCm/flash-attention.git
cd flash-attention
git checkout b7d29fb
git submodule update --init
MAX_JOBS=104 GPU_ARCHS="gfx942" python3 setup.py install
cd ..

# Xformers Install from source
git clone https://github.com/ROCm/xformers.git
cd xformers/
git submodule update --init --recursive
PYTORCH_ROCM_ARCH=gfx942 python3 setup.py install #Instinct MI300-series

# rocm driver may need to install from scratch to work
export PYTORCH_ROCM_ARCH="gfx942"
git clone https://github.com/ROCm/vllm.git
cd vllm
pip install amdsmi
pip install --upgrade numba scipy huggingface-hub[cli,hf_transfer] setuptools_scm
pip install "numpy<2"
pip install -r requirements/rocm.txt
sudo apt install libstdc++-12-dev -y
python3 setup.py develop
cd ..


# bitsandbytes
rm -rf bitsandbytes
git clone https://github.com/ROCm/bitsandbytes.git  
cd bitsandbytes/
python3.10 -m pip install -r requirements-dev.txt
cmake -DCOMPUTE_BACKEND=cuda -S .
make
python3.10 -m pip install -e .
cd ..


git clone https://github.com/radna0/ms-swift.git && \
cd ms-swift && \
git pull && \
pip install . && \ 
pip install setuptools -U && \
cd ..


pip install git+https://github.com/huggingface/trl.git && \
pip install math-verify==0.5.2 hf_transfer wandb && \
pip uninstall setuptools -y && \
pip install setuptools==69.0.0 && \
pip uninstall deepspeed -y && \
pip install deepspeed -U && \
pip install setuptools -U && \
pip install --upgrade pillow


pip install transformers pandas polars numpy huggingface_hub[hf_transfer] wandb accelerate deepspeed datasets flashinfer-python pybind11


huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec


amd-smi version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version











