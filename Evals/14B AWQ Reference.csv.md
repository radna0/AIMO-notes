

```

os.environ["TRITON_PTXAS_PATH"] = "/usr/local/cuda/bin/ptxas"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["VLLM_USE_V1"]='1'


################################################################ NEW BEST?
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192

Maximum concurrency for 8192 tokens per request: 34.61x

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

19 Result? in 7:30 mins


##############
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192 * 3 // 2

Maximum concurrency for 12288 tokens per request: 23.07x

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

31 Result? in 9:30 mins







##############
MAX_NUM_SEQS = 24
MAX_MODEL_LEN = 8192 * 3 // 2

Maximum concurrency for 12288 tokens per request: 23.07x

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '177']
180

22 Result? in 7:18 mins



#############################################
MAX_NUM_SEQS = 24
MAX_MODEL_LEN = 10 * 1024

Maximum concurrency for 10240 tokens per request: 27.69x

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

20 Result? in 6:30 mins


#######################################################

MAX_NUM_SEQS = 24
MAX_MODEL_LEN = 8192

Maximum concurrency for 8192 tokens per request: 34.61x

Total predictions compared: 10
Number of correct predictions: 5
Accuracy: 50.00%

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

17 Result? in 5:30 mins

#############################################
MAX_NUM_SEQS = 20
MAX_MODEL_LEN = 8192 * 3 // 2

Maximum concurrency for 12288 tokens per request: 23.07x

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

19 Result? in 7:06 mins


#############################################
MAX_NUM_SEQS = 20
MAX_MODEL_LEN = 10 * 1024

Maximum concurrency for 10240 tokens per request: 27.69x

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

18 Result? in 6:25 mins


################################################################ BEST PERF
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192 * 3 // 2

Maximum concurrency for 12288 tokens per request: 23.07x

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

13 Result in 06:32 mins

Total predictions compared: 10
Number of correct predictions: 7
Accuracy: 70.00%

Incorrect predictions:
       id  \
0  057f8a   
5  480182   
7  88c219   

                                                                                                                                                                                                                                                                                                                                                                                                                    question  \
0  Three airline companies operate flights from Dodola island. Each company has a different schedule of departures. The first company departs every 100 days, the second every 120 days and the third every 150 days. What is the greatest positive integer $d$ for which it is true that there will be $d$ consecutive days without a flight from Dodola island, regardless of the departure times of the various airlines?   
5       Let $ABC$ be a triangle with $BC=108$, $CA=126$, and $AB=39$. Point $X$ lies on segment $AC$ such that $BX$ bisects $\angle CBA$. Let $\omega$ be the circumcircle of triangle $ABX$. Let $Y$ be a point on $\omega$ different from $X$ such that $CX=CY$. Line $XY$ meets $BC$ at $E$. The length of the segment $BE$ can be written as $\frac{m}{n}$, where $m$ and $n$ are coprime positive integers. Find $m+n$.   
7         For positive integers $x_1,\ldots, x_n$ define $G(x_1, \ldots, x_n)$ to be the sum of their $\frac{n(n-1)}{2}$ pairwise greatest common divisors. We say that an integer $n \geq 2$ is \emph{artificial} if there exist $n$ different positive integers $a_1, ..., a_n$ such that \n\[a_1 + \cdots + a_n = G(a_1, \ldots, a_n) +1.\]\nFind the sum of all artificial integers $m$ in the range $2 \leq m \leq 40$.   

   answer_ref  answer_pred  
0          79           99  
5         751          210  
7         810           13


##############################
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192

Maximum concurrency for 8192 tokens per request: 34.61x

['180', '180', '180', '180', '180', '180', '180', '180', '180']
180

9 Resuit? in 4:36 mins

#############
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 1024 * 3 // 2

Maximum concurrency for 12288 tokens per request: 23.07x

[]
210

0 Result in 00:37 mins




################################################################ BEST SPEED
MAX_NUM_SEQS = 12
MAX_MODEL_LEN = 8192 * 3 // 2

Processed prompts: 100%|██████████| 12/12 [05:08<00:00, 25.74s/it, est. speed input: 4.86 toks/s, output: 310.56 toks/s]

['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

Total Time for first prediction: Roughly 11 mins


```



```

os.environ["TRITON_PTXAS_PATH"] = "/usr/local/cuda/bin/ptxas"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["VLLM_USE_V1"]='1'

os.environ["VLLM_ATTENTION_BACKEND"]='FLASHINFER'
os.environ["VLLM_USE_FLASHINFER_SAMPLER"]='1'
os.environ["VLLM_FLASHINFER_FORCE_TENSOR_CORES"]='1'


################################################################
MAX_NUM_SEQS = 12
MAX_MODEL_LEN = 8192 * 3 // 2

Processed prompts: 100%|██████████| 12/12 [05:08<00:00, 25.70s/it, est. speed input: 4.86 toks/s, output: 310.98 toks/s]


['180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180', '180']
180

Total Time for first prediction: 12 mins



```

