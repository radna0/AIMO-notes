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
pip uninstall -y triton flash_attn vllm


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
MAX_JOBS=104 GPU_ARCHS="gfx942" python3 setup.py install
cd ..

# Xformers Install from source
git clone https://github.com/ROCm/xformers.git
cd xformers/
git submodule update --init --recursive
PYTORCH_ROCM_ARCH=gfx942 python setup.py install #Instinct MI300-series

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


# Clone TE repo and submodules
sudo apt-get install liblzma-dev pkg-config
export HIP_PATH=/opt/rocm
export ROCM_PATH=/opt/rocm
export PATH=$ROCM_PATH/bin:$PATH
export LD_LIBRARY_PATH=$ROCM_PATH/lib:$LD_LIBRARY_PATH

git clone --recursive https://github.com/ROCm/TransformerEngine.git

cd TransformerEngine
export NVTE_FRAMEWORK=pytorch #optionally set framework, currently only support pytorch and jax; if not set will try to detect installed frameworks
export NVTE_ROCM_ARCH=gfx942 # CK fused attn only support MI200 and MI300 and fp8 features are only supported on MI300

# Build Platform Selection (optional)
# Note: Useful when both ROCm and CUDA platforms are present in the Docker
export NVTE_USE_ROCM=1  #Use 1 for ROCm, or set to 0 to use CUDA; If not set will try to detect installed platform, prioritizing ROCm

pip install .


# git clone https://github.com/radna0/open-r1.git
# cd open-r1
# GIT_LFS_SKIP_SMUDGE=1 python3.10 -m pip install -e ".[dev]"
# cd ..



huggingface-cli login --token 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
wandb login e2ed6858c3226f51a97cdffcb81282ee2164bcec


amd-smi version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version