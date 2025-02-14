


## 3 English prompt

```
os.environ["TRITON_PTXAS_PATH"] = "/usr/local/cuda/bin/ptxas"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["VLLM_USE_V1"]='0'


#############################################
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192 * 3 // 2

Processed prompts: 100%|██████████| 16/16 [10:01<00:00, 37.62s/it, est. speed input: 3.29 toks/s, output: 196.52 toks/s] 

494, 5994, 6606, 6692, 6889, 7043, 7274, 8579, 8617, 10996, 11498, 12165]
['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

```



```

os.environ["TRITON_PTXAS_PATH"] = "/usr/local/cuda/bin/ptxas"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["VLLM_USE_V1"]='1'

os.environ["VLLM_ATTENTION_BACKEND"]='FLASHINFER'
os.environ["VLLM_USE_FLASHINFER_SAMPLER"]='1'
os.environ["VLLM_FLASHINFER_FORCE_TENSOR_CORES"]='1'


#############################################
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192 * 3 // 2

Processed prompts: 100%|██████████| 16/16 [08:50<00:00, 33.18s/it, est. speed input: 3.74 toks/s, output: 222.97 toks/s]

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180




##############################
MAX_NUM_SEQS = 12
MAX_MODEL_LEN = 8192 * 3 // 2
Processed prompts: 100%|██████████| 12/12 [08:59<00:00, 44.94s/it, est. speed input: 2.76 toks/s, output: 159.40 toks/s]

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180




################################################################

MAX_NUM_SEQS = 12
MAX_MODEL_LEN = 8192
Processed prompts: 100%|██████████| 16/16 [07:02<00:00, 26.43s/it, est. speed input: 4.69 toks/s, output: 264.89 toks/s]


['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180


```

