
## amd/Llama-3.1-70B-Instruct-FP8-KV
```
VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=0 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.05 --top_k 50 > evals_log/0.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%
Time Taken: 1761.65358543396

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=0 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k 50 > evals_log/0.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%
Time Taken: 1761.65358543396

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=1 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 4096 --quant_policy 0 --min_p 0.05 --top_k 50 > evals_log/1.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 2658.7013795375824

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=2 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 4096 --quant_policy 0 --min_p 0.10 --top_k 50 > evals_log/2.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 9
Accuracy: 18.00%
Time Taken: 2892.9366915225983

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=3 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.05 --top_k 50 > evals_log/3.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 11
Accuracy: 22.00%

Time Taken: 3127.127448320389

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=4 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.10 --top_k 50 > evals_log/4.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 11
Accuracy: 22.00%
Time Taken: 3430.6463260650635

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=5 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/5.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 3352.927845954895

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=6 python eval_vllm.py --model amd/Llama-3.1-70B-Instruct-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/6.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 12
Accuracy: 24.00%
Time Taken: 2796.7826364040375

```



## radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV

```
VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=7 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.05 --top_k 50 > evals_log/7.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 9
Accuracy: 18.00%
Time Taken: 1889.726687669754
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=0 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k 50 > evals_log/0.log 2>&1 &
  

Total predictions compared: 50
Number of correct predictions: 7
Accuracy: 14.00%
Time Taken: 2008.5577218532562
######################################################################
  

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=1 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 4096 --quant_policy 0 --min_p 0.05 --top_k 50 > evals_log/1.log 2>&1 &


Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 2329.894767522812
######################################################################


VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=2 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 4096 --quant_policy 0 --min_p 0.10 --top_k 50 > evals_log/2.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 2352.6672484874725
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=3 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.05 --top_k 50 > evals_log/3.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 2131.358342885971
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=4 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.10 --top_k 50 > evals_log/4.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 9
Accuracy: 18.00%
Time Taken: 2260.514716863632
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=5 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/5.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 9
Accuracy: 18.00%
Time Taken: 2380.2850852012634
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=6 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 6144 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/6.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 2549.084203004837





######################################################################
######################################################################
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=0 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 2048 --quant_policy 0 --min_p 0.5 --top_k -1 > evals_log/0.log 2>&1 &

Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 1952.8688704967499

######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=1 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 2048 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/1.log 2>&1 &


Total predictions compared: 50
Number of correct predictions: 9
Accuracy: 18.00%
Time Taken: 1946.8833322525024

######################################################################
  

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=2 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 4096 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/2.log 2>&1 &

  
Total predictions compared: 50
Number of correct predictions: 10
Accuracy: 20.00%
Time Taken: 2019.8719549179077

######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=3 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 16 --tokens 4096 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/3.log 2>&1 &

  
  
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=4 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 32 --tokens 2048 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/4.log 2>&1 &

  
  
######################################################################

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=5 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 32 --tokens 2048 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/5.log 2>&1 &

  
######################################################################
  

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=6 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 32 --tokens 4096 --quant_policy 0 --min_p 0.05 --top_k -1 > evals_log/6.log 2>&1 &

  
######################################################################
  

VLLM_USE_TRITON_FLASH_ATTN=0 ROCR_VISIBLE_DEVICES=7 python eval_vllm.py --model radna/Llama-3.1-Nemotron-70B-Instruct-HF-FP8-KV --file hard_batch_1.csv --num_seqs 32 --tokens 4096 --quant_policy 0 --min_p 0.10 --top_k -1 > evals_log/7.log 2>&1 &
```

