accelerate launch --config_file=../../recipes/accelerate_configs/zero2.yaml \
    --num_processes=1 grpo.py \
    --config ../../recipes/DeepSeek-R1-Distill-Qwen-1.5B/grpo/config_7b_gh200.yaml
    --resume_from_checkpoint=data/DeepSeek-R1-Distill-Qwen-14B-GRPO-LIMO/$3"


accelerate launch --config_file=recipes/accelerate_configs/zero2.yaml \
    --num_processes=1 src/open_r1/grpo.py \
    --config recipes/DeepSeek-R1-Distill-Qwen-1.5B/grpo/config_7b_gh200.yaml
    --resume_from_checkpoint=data/DeepSeek-R1-Distill-Qwen-7B-GRPO-LIMO/$3"
