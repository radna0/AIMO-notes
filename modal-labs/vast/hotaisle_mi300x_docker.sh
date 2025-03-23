# # For quick & easy docker install:
# Get the install script file
curl -fsSL https://get.docker.com -o get-docker.sh
# Run the script
sh get-docker.sh

sudo apt update && sudo apt upgrade -y
sudo apt install --install-recommends linux-generic

sudo dockerd

# Test env
amd-smi version
python3.10 --version
python3.10 -c "import torch; print(torch.__version__)"
git-lfs --version

# Training

docker pull rocm/pytorch-training:v25.4

docker build -t rocm_training .

docker stop training_env
docker rm training_env

docker run -it --workdir /storage/ --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v /mnt/nvme5n1p1:/storage -v $HOME:$HOME -v  $HOME/.ssh:/root/.ssh --shm-size 512G --name training_env rocm_training

pip install git+https://github.com/huggingface/trl.git

VLLM_USE_TRITON_FLASH_ATTN=0 HF_HOME=cache/ mergekit-evolve --vllm --task-search-path /home/hotaisle/lm-evaluation-harness/lm_eval/tasks/aime --max-fevals 96 --force-population-size 8 --strategy pool --storage-path /storage/Qwen-32B-merge --num-gpus 8 --trust-remote-code --wandb --i-understand-the-depths-of-the-evils-i-am-unleashing --batch-size 1 Fuse-DeepSeek-R1-32B.yaml >> merge_logs.log 2>&1 &



AMD_SERIALIZE_KERNEL=1 \
HF_HUB_ENABLE_HF_TRANSFER=1 \
VLLM_USE_TRITON_FLASH_ATTN=0 \
OMP_NUM_THREADS=13 \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=8  \
swift rlhf \
    --rlhf_type grpo \
    --model /storage/distill-14b \
    --resume_from_checkpoint /storage/trained_grpo_distill_14b/v46-20250318-203931/checkpoint-22 \
    --resume_only_model \
    --model_type deepseek_r1_distill \
    --use_hf true \
    --async_generate false \
    --num_infer_workers 8 \
    --num_iterations 2 \
    --reward_funcs cosine \
    --cosine_max_len 12288 \
    --cosine_min_len_value_correct 0.8 \
    --cosine_max_len_value_correct 0.4 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -0.2 \
    --train_type lora \
    --lora_rank 32 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --torch_dtype bfloat16 \
    --dataset GAIR/LIMO \
    --max_completion_length 12288 \
    --num_train_epochs 5 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 1 \
    --learning_rate 1e-4 \
    --gradient_accumulation_steps 4 \
    --eval_steps 4 \
    --save_steps 4 \
    --save_total_limit 100 \
    --logging_steps 1 \
    --report_to wandb \
    --max_length 16384 \
    --output_dir /storage/trained_grpo_distill_14b \
    --warmup_ratio 0.1 \
    --num_generations 2 \
    --temperature 1.0 \
    --top_p 0.90 \
    --top_k 50 \
    --repetition_penalty 1.1 \
    --deepspeed zero2 \
    --system 'You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}.' \
    --log_completions true \
    --dataloader_num_workers 52 \
    --dataset_num_proc 52 \
    >> train_logs.log 2>&1 &


################################################################
#### SECOND STAGE RL 


AMD_SERIALIZE_KERNEL=1 \
HF_HUB_ENABLE_HF_TRANSFER=1 \
VLLM_USE_TRITON_FLASH_ATTN=0 \
OMP_NUM_THREADS=13 \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=8  \
swift rlhf \
    --rlhf_type grpo \
    --model /storage/fused-14b-SFT288-RL60 \
    --model_type deepseek_r1_distill \
    --use_hf true \
    --async_generate false \
    --num_infer_workers 8 \
    --num_iterations 1 \
    --reward_funcs cosine repetition \
    --cosine_max_len 12288 \
    --cosine_min_len_value_correct 1 \
    --cosine_max_len_value_correct 0.5 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -0.25 \
    --repetition_n_grams 40 \
    --repetition_max_penalty -0.05 \
    --train_type lora \
    --lora_rank 32 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --torch_dtype bfloat16 \
    --dataset 'hard_batch_234.jsonl' \
    --val_dataset 'hard_batch_1.jsonl' \
    --max_completion_length 12288 \
    --num_train_epochs 10 \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 1 \
    --learning_rate 1e-4 \
    --gradient_accumulation_steps 4 \
    --save_strategy 'epoch' \
    --save_total_limit 100 \
    --logging_steps 1 \
    --report_to wandb \
    --max_length 16384 \
    --output_dir /storage/trained_grpo_fused_14b_SFT288_RL60 \
    --warmup_ratio 0.1 \
    --num_generations 4 \
    --temperature 1.0 \
    --top_p 0.90 \
    --top_k 50 \
    --repetition_penalty 1.1 \
    --deepspeed zero2 \
    --system 'You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}.' \
    --log_completions true \
    --dataloader_num_workers 52 \
    --dataset_num_proc 52 \
    >> train_logs_4.log 2>&1 &

################################################################


 /storage/omnitrace/bin/omnitrace-python-3.10 -- \



export NNODES=1
export NODE_RANK=0
export MASTER_ADDR=127.0.0.1
export MASTER_PORT=29500




watch -n0 tail train_logs_multi_rl.log

# Enter evey node, and export each batch of commands for that node
export NNODES=4
export NODE_RANK=0
export MASTER_ADDR=127.0.0.1
export MASTER_PORT=29500


export NNODES=4
export NODE_RANK=1
export MASTER_ADDR=192.168.0.205
export MASTER_PORT=29500

export NNODES=4
export NODE_RANK=2
export MASTER_ADDR=192.168.0.205
export MASTER_PORT=29500

export NNODES=4
export NODE_RANK=3
export MASTER_ADDR=192.168.0.205
export MASTER_PORT=29500


################### STAGE 1, PRIMING
    --cosine_min_len_value_correct 0.5 \
    --cosine_max_len_value_correct 0.25 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -1 \

################### STAGE 2, WALKING
    --cosine_min_len_value_correct 1 \
    --cosine_max_len_value_correct 0.5 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -1 \

################### STAGE 3, RUNNING
    --cosine_min_len_value_correct 1 \
    --cosine_max_len_value_correct 0.5 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -0.5 \


AMD_SERIALIZE_KERNEL=1 \
HF_HUB_ENABLE_HF_TRANSFER=1 \
VLLM_USE_TRITON_FLASH_ATTN=0 \
OMP_NUM_THREADS=13 \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=8  \
swift rlhf \
    --rlhf_type grpo \
    --model /storage/fuse-32b \
    --model_type deepseek_r1_distill \
    --use_hf true \
    --async_generate false \
    --num_infer_workers 8 \
    --num_iterations 2 \
    --reward_funcs cosine repetition \
    --cosine_max_len 12288 \
    --cosine_min_len_value_correct 0.5 \
    --cosine_max_len_value_correct 0.25 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -1 \
    --repetition_n_grams 40 \
    --repetition_max_penalty -0.05 \
    --train_type lora \
    --lora_rank 32 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --torch_dtype bfloat16 \
    --dataset stage1_aime.jsonl \
    --val_dataset eval_aime.jsonl \
    --max_completion_length 12288 \
    --num_train_epochs 5 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --learning_rate 1e-4 \
    --gradient_accumulation_steps 4 \
    --save_steps 4 \
    --eval_steps 12 \
    --save_total_limit 100 \
    --logging_steps 1 \
    --report_to wandb \
    --max_length 16384 \
    --output_dir /storage/trained_grpo_fuse_32b \
    --warmup_ratio 0.1 \
    --num_generations 4 \
    --temperature 1.0 \
    --top_p 0.90 \
    --top_k 50 \
    --repetition_penalty 1.1 \
    --deepspeed zero2 \
    --system 'You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}.' \
    --log_completions true \
    --dataloader_num_workers 104 \
    --dataset_num_proc 104 \
    > train_logs_multi_rl.log 2>&1 &


################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################

AMD_SERIALIZE_KERNEL=1 \
HF_HUB_ENABLE_HF_TRANSFER=1 \
VLLM_USE_TRITON_FLASH_ATTN=0 \
OMP_NUM_THREADS=13 \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=8  \
swift rlhf \
    --rlhf_type grpo \
    --model /storage/fuse-32b \
    --model_type deepseek_r1_distill \
    --use_hf true \
    --async_generate false \
    --num_infer_workers 8 \
    --num_iterations 2 \
    --reward_funcs cosine repetition \
    --cosine_max_len 12288 \
    --cosine_min_len_value_correct 1 \
    --cosine_max_len_value_correct 0.5 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -1 \
    --repetition_n_grams 40 \
    --repetition_max_penalty -0.05 \
    --train_type lora \
    --lora_rank 32 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --torch_dtype bfloat16 \
    --dataset stage2_aime.jsonl \
    --val_dataset eval_aime.jsonl \
    --max_completion_length 12288 \
    --num_train_epochs 5 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --learning_rate 1e-4 \
    --gradient_accumulation_steps 4 \
    --save_strategy 'epoch' \
    --save_total_limit 100 \
    --logging_steps 1 \
    --report_to wandb \
    --max_length 16384 \
    --output_dir /storage/trained_grpo_fuse_32b \
    --warmup_ratio 0.1 \
    --num_generations 4 \
    --temperature 1.0 \
    --top_p 0.90 \
    --top_k 50 \
    --repetition_penalty 1.1 \
    --deepspeed zero2 \
    --system 'You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}.' \
    --log_completions true \
    --dataloader_num_workers 104 \
    --dataset_num_proc 104 \
    > train_logs_multi_rl.log 2>&1 &

################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################

AMD_SERIALIZE_KERNEL=1 \
HF_HUB_ENABLE_HF_TRANSFER=1 \
VLLM_USE_TRITON_FLASH_ATTN=0 \
OMP_NUM_THREADS=13 \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=8  \
swift rlhf \
    --rlhf_type grpo \
    --model /storage/fuse-32b \
    --model_type deepseek_r1_distill \
    --use_hf true \
    --async_generate false \
    --num_infer_workers 8 \
    --num_iterations 2 \
    --reward_funcs cosine repetition \
    --cosine_max_len 12288 \
    --cosine_min_len_value_correct 1 \
    --cosine_max_len_value_correct 0.5 \
    --cosine_max_len_value_wrong 0 \
    --cosine_min_len_value_wrong -0.5 \
    --repetition_n_grams 40 \
    --repetition_max_penalty -0.05 \
    --train_type lora \
    --lora_rank 32 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --torch_dtype bfloat16 \
    --dataset stage3_aime.jsonl \
    --val_dataset eval_aime.jsonl \
    --max_completion_length 12288 \
    --num_train_epochs 5 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --learning_rate 1e-4 \
    --gradient_accumulation_steps 4 \
    --save_strategy 'epoch' \
    --save_total_limit 100 \
    --logging_steps 1 \
    --report_to wandb \
    --max_length 16384 \
    --output_dir /storage/trained_grpo_fuse_32b \
    --warmup_ratio 0.1 \
    --num_generations 4 \
    --temperature 1.0 \
    --top_p 0.90 \
    --top_k 50 \
    --repetition_penalty 1.1 \
    --deepspeed zero2 \
    --system 'You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}.' \
    --log_completions true \
    --dataloader_num_workers 104 \
    --dataset_num_proc 104 \
    > train_logs_multi_rl.log 2>&1 &



################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################
################################################################


    --resume_from_checkpoint /storage/trained_grpo_fuse_32b \




HF_HUB_ENABLE_HF_TRANSFER=1 \
OMP_NUM_THREADS=13 \
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
NPROC_PER_NODE=8  \
swift sft \
    --model /storage/fuse-32b \
    --model_type deepseek_r1_distill \
    --use_hf true \
    --train_type lora \
    --lora_rank 32 \
    --lora_alpha 32 \
    --target_modules all-linear \
    --torch_dtype bfloat16 \
    --dataset radna/final-stage2-3k.jsonl \
    --num_train_epochs 10 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 2 \
    --learning_rate 1e-5 \
    --gradient_accumulation_steps 4 \
    --save_strategy 'epoch' \
    --save_total_limit 30 \
    --logging_steps 1 \
    --report_to wandb \
    --max_length 12288 \
    --output_dir /storage/trained-sft-lora-fuse-32b \
    --warmup_ratio 0.1 \
    --deepspeed zero2 \
    --dataloader_num_workers 104 \
    --dataset_num_proc 104 \
    > train_logs_multi_sft.log 2>&1 &




docker pull rocm/vllm:rocm6.3.1_instinct_vllm0.7.3_20250311


cd /mnt/nvme5n1p1

docker build -t rocm-dev .

docker run -it --workdir /storage/ --device /dev/dri --device /dev/kfd --network host --ipc host --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined --privileged -v /mnt/nvme5n1p1:/storage -v $HOME:$HOME -v  $HOME/.ssh:/root/.ssh --shm-size 512G --name rocm_dev_container rocm-dev

docker exec -it rocm_dev_container bash

docker stop rocm_dev_container
docker rm rocm_dev_container


huggingface-cli download radna/test_final_limo.jsonl --local-dir /storage --repo-type dataset
huggingface-cli download radna/hard_batch_1.jsonl --local-dir /storage --repo-type dataset