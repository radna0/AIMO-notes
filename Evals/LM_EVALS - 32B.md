
# gsm8k

```

lm_eval   --model vllm   --model_args pretrained=casperhansen/deepseek-r1-distill-qwen-32b-awq,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.864|±  |0.0217|
|     |       |strict-match    |     5|exact_match|↑  |0.856|±  |0.0222|

#########################################################################

lm_eval   --model vllm   --model_args pretrained=Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.820|±  |0.0243|
|     |       |strict-match    |     5|exact_match|↑  |0.852|±  |0.0225|

#########################################################################

lm_eval   --model vllm   --model_args pretrained=Qwen/QwQ-32B-AWQ,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.532|±  |0.0316|
|     |       |strict-match    |     5|exact_match|↑  |0.700|±  |0.0290|

```


# gsm8k,asdiv,hendrycks_math,mathqa
```

lm_eval   --model vllm   --model_args pretrained=casperhansen/deepseek-r1-distill-qwen-32b-awq,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10



|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0000|±  |0.0000|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.9174|±  |0.0076|
|                                      |       |strict-match    |    10|exact_match|↑  |0.9113|±  |0.0078|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.3132|±  |0.0064|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.3454|±  |0.0138|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.3038|±  |0.0211|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2797|±  |0.0205|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.2082|±  |0.0135|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.2315|±  |0.0182|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.4776|±  |0.0169|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2729|±  |0.0191|
|mathqa                                |      1|none            |    10|acc        |↑  |0.6023|±  |0.0090|
|                                      |       |none            |    10|acc_norm   |↑  |0.6121|±  |0.0089|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.3132|±  |0.0064|


#########################################################################

lm_eval   --model vllm   --model_args pretrained=Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10


|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0000|±  |0.0000|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.9287|±  |0.0071|
|                                      |       |strict-match    |    10|exact_match|↑  |0.9227|±  |0.0074|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.3078|±  |0.0064|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.3404|±  |0.0138|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.3165|±  |0.0214|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2714|±  |0.0203|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1938|±  |0.0132|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.2315|±  |0.0182|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.4684|±  |0.0169|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2692|±  |0.0190|
|mathqa                                |      1|none            |    10|acc        |↑  |0.6037|±  |0.0090|
|                                      |       |none            |    10|acc_norm   |↑  |0.6137|±  |0.0089|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.3078|±  |0.0064|



#########################################################################


lm_eval   --model vllm   --model_args pretrained=Qwen/QwQ-32B-AWQ,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.7748|±  |0.0115|
|                                      |       |strict-match    |    10|exact_match|↑  |0.7043|±  |0.0126|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2834|±  |0.0063|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.3075|±  |0.0134|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.2447|±  |0.0198|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2610|±  |0.0201|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1816|±  |0.0128|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.2278|±  |0.0181|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.4535|±  |0.0169|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2363|±  |0.0182|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5933|±  |0.0090|
|                                      |       |none            |    10|acc_norm   |↑  |0.6030|±  |0.0090|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2834|±  |0.0063|


```



# gsm8k - LMDeploy Quants

```

lm_eval   --model vllm   --model_args pretrained=radna/fused-r1-32b-awq-max,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250


|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.856|±  |0.0222|
|     |       |strict-match    |     5|exact_match|↑  |0.872|±  |0.0212|

#########################################################################

lm_eval  --model vllm  --model_args pretrained=radna/NEW-Fuse-Hendrycks-1-awq-max,add_bos_token=True  --tasks gsm8k,asdiv,hendrycks_math,mathqa --batch_size auto --trust_remote_code --num_fewshot 10



```

# gsm8k,asdiv,hendrycks_math,mathqa - LMDeploy Quants

```

lm_eval   --model vllm   --model_args pretrained=radna/fused-r1-32b-awq-max,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10


|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0000|±  |0.0000|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.9287|±  |0.0071|
|                                      |       |strict-match    |    10|exact_match|↑  |0.9204|±  |0.0075|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.3132|±  |0.0064|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.3446|±  |0.0138|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.2932|±  |0.0209|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2818|±  |0.0206|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.2071|±  |0.0135|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.2370|±  |0.0183|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.4742|±  |0.0169|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2839|±  |0.0193|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5973|±  |0.0090|
|                                      |       |none            |    10|acc_norm   |↑  |0.6070|±  |0.0089|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.3132|±  |0.0064|


#########################################################################

lm_eval  --model vllm  --model_args pretrained=radna/NEW-Fuse-Hendrycks-1-awq-max,add_bos_token=True  --tasks gsm8k,asdiv,hendrycks_math,mathqa --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.9158|±  |0.0076|
|                                      |       |strict-match    |    10|exact_match|↑  |0.9105|±  |0.0079|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.3596|±  |0.0067|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.3842|±  |0.0141|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.3713|±  |0.0222|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.3257|±  |0.0214|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.2492|±  |0.0144|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.2852|±  |0.0194|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.5247|±  |0.0169|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.3187|±  |0.0200|
|mathqa                                |      1|none            |    10|acc        |↑  |0.6489|±  |0.0087|
|                                      |       |none            |    10|acc_norm   |↑  |0.6600|±  |0.0087|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.3596|±  |0.0067|


#########################################################################

lm_eval  --model vllm  --model_args pretrained=radna/NEW-Fuse-32B-ALL-awq-max,add_bos_token=True  --tasks gsm8k,asdiv,hendrycks_math,mathqa --batch_size auto --trust_remote_code --num_fewshot 10


|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.9090|±  |0.0079|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8931|±  |0.0085|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.3602|±  |0.0067|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.3850|±  |0.0141|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.3776|±  |0.0223|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.3319|±  |0.0215|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.2492|±  |0.0144|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.2815|±  |0.0194|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.5235|±  |0.0169|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.3168|±  |0.0199|
|mathqa                                |      1|none            |    10|acc        |↑  |0.6489|±  |0.0087|
|                                      |       |none            |    10|acc_norm   |↑  |0.6630|±  |0.0087|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.3602|±  |0.0067|

#########################################################################

(FIXED TOKENIZER) lm_eval  --model vllm  --model_args pretrained=radna/NEW-Fuse-DeepSeek-R1-AIME-1-awq-max  --tasks gsm8k,asdiv,hendrycks_math,mathqa --batch_size auto --trust_remote_code --num_fewshot 10



|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0000|±  |0.0000|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.9272|±  |0.0072|
|                                      |       |strict-match    |    10|exact_match|↑  |0.9227|±  |0.0074|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.3636|±  |0.0067|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.3850|±  |0.0141|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.3840|±  |0.0224|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.3257|±  |0.0214|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.2547|±  |0.0145|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.2889|±  |0.0195|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.5327|±  |0.0169|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.3168|±  |0.0199|
|mathqa                                |      1|none            |    10|acc        |↑  |0.6456|±  |0.0088|
|                                      |       |none            |    10|acc_norm   |↑  |0.6566|±  |0.0087|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.3636|±  |0.0067|

```