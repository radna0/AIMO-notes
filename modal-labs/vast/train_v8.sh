accelerate launch --config_file=recipes/accelerate_configs/zero2.yaml \
    --num_processes=7 src/open_r1/grpo.py \
    --config recipes/DeepSeek-R1-Distill-Qwen-1.5B/grpo/config_7b_v8.yaml
    --resume_from_checkpoint=data/DeepSeek-R1-Distill-Qwen-7B-GRPO-LIMO/$3"
