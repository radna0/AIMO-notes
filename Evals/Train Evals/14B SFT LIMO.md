

```
VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=0 python eval_vllm.py --checkpoint --model  /storage/distill-14b --file hard_batch_1.csv --num_seqs 16 --tokens 12288 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/0.log 2>&1 &

Perplexity: 8.922447204589844
AFTER Perplexity: 9.027137756347656

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=1 python eval_vllm.py --checkpoint --model  /storage/distill-14b --file hard_batch_1.csv --num_seqs 16 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/1.log 2>&1 &

#########################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=2 python eval_vllm.py --checkpoint --model  /storage/trained-sft-distill-14b/v8-20250316-122710/checkpoint-36-merged --file hard_batch_1.csv --num_seqs 16 --tokens 12288 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/2.log 2>&1 &

Perplexity: 8.54992389678955
AFTER Perplexity: 8.657190322875977

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=3 python eval_vllm.py --checkpoint --model  /storage/trained-sft-distill-14b/v8-20250316-122710/checkpoint-36-merged --file hard_batch_1.csv --num_seqs 16 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/3.log 2>&1 &

#########################################################################
  

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=4 python eval_vllm.py --checkpoint --model  /storage/trained-sft-distill-14b/v8-20250316-122710/checkpoint-72-merged --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/4.log 2>&1 &

Perplexity: 8.476582527160645  
AFTER Perplexity: 8.569162368774414

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=5 python eval_vllm.py --checkpoint --model  /storage/trained-sft-distill-14b/v8-20250316-122710/checkpoint-72-merged --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/5.log 2>&1 &

  
#########################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=6 python eval_vllm.py --checkpoint --model  /storage/trained-sft-distill-14b/v8-20250316-122710/checkpoint-108-merged --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/6.log 2>&1 &

Perplexity: 8.753617286682129  
AFTER Perplexity: 8.789289474487305

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=7 python eval_vllm.py --checkpoint --model  /storage/trained-sft-distill-14b/v8-20250316-122710/checkpoint-108-merged --file hard_batch_1.csv --num_seqs 32 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/7.log 2>&1 &



#########################################################################





144


Perplexity: 9.23083209991455
AFTER Perplexity: 9.26249885559082


180 

Perplexity: 9.711173057556152
AFTER Perplexity: 9.753877639770508

216 

Perplexity: 9.975035667419434
AFTER Perplexity: 10.041444778442383

252

Perplexity: 10.173410415649414

AFTER Perplexity: 10.223067283630371


288
Perplexity: 10.25429630279541
AFTER Perplexity: 10.450393676757812

```