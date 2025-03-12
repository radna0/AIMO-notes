# # For quick & easy docker install:
# Get the install script file
curl -fsSL https://get.docker.com -o get-docker.sh
# Run the script
sh get-docker.sh

sudo apt update && sudo apt upgrade -y
sudo apt install --install-recommends linux-generic

sudo dockerd

# Training

docker build -t my_rocm_training_env .

docker stop training_env
docker rm training_env

docker run -it --workdir /home/hotaisle/eval --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v /mnt/nvme5n1p1:/storage -v $HOME:$HOME -v  $HOME/.ssh:/root/.ssh --shm-size 512G --name training_env my_rocm_training_env



VLLM_USE_TRITON_FLASH_ATTN=0 HF_HOME=cache/ mergekit-evolve --vllm --task-search-path /home/hotaisle/lm-evaluation-harness/lm_eval/tasks/aime --max-fevals 96 --force-population-size 8 --strategy pool --storage-path /storage/Qwen-32B-merge --num-gpus 8 --trust-remote-code --wandb --i-understand-the-depths-of-the-evils-i-am-unleashing --batch-size 1 Fuse-DeepSeek-R1-32B.yaml >> merge_logs.log 2>&1 &









VLLM_USE_TRITON_FLASH_ATTN=0 python unsloth_train.py  >> unsloth_logs.log 2>&1 &
watch -n0 unsloth_logs.log


# vLLM Inference 
docker pull rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6

docker run -it --workdir /home/hotaisle/eval --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v $HOME:$HOME -v  $HOME/.ssh:/root/.ssh --shm-size 64G --name inference_env rocm/vllm:rocm6.3.1_mi300_ubuntu22.04_py3.12_vllm_0.6.6

docker rm inference_env