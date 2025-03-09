
# gsm8k

`lm_eval   --model vllm   --model_args pretrained=model,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250 
```

neuralmagic/DeepSeek-R1-Distill-Qwen-14B-FP8-dynamic

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.880|±  |0.0206|
|     |       |strict-match    |     5|exact_match|↑  |0.888|±  |0.0200|

#########################################################################

deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.864|±  |0.0217|
|     |       |strict-match    |     5|exact_match|↑  |0.876|±  |0.0209|

#########################################################################

Jianyuan1/deepseek-r1-14b-cot-math-reasoning-full

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.888|±  |0.0200|
|     |       |strict-match    |     5|exact_match|↑  |0.896|±  |0.0193|

#########################################################################

neuralmagic/DeepSeek-R1-Distill-Qwen-14B-quantized.w8a8

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.900|±  |0.0190|
|     |       |strict-match    |     5|exact_match|↑  |0.908|±  |0.0183|

#########################################################################

neuralmagic/DeepSeek-R1-Distill-Qwen-14B-quantized.w4a16

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.808|±  | 0.025|
|     |       |strict-match    |     5|exact_match|↑  |0.900|±  | 0.019|


##########################################################################

radna/deepseek-14b-dyve-awq

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.880|±  |0.0206|
|     |       |strict-match    |     5|exact_match|↑  |0.872|±  |0.0212|

#########################################################################

neody/r1-14b-awq

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.876|±  |0.0209|
|     |       |strict-match    |     5|exact_match|↑  |0.880|±  |0.0206|

```


# gsm8k,asdiv,hendrycks_math,mathqa
`lm_eval   --model vllm   --model_args pretrained=model,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 0
```

neuralmagic/DeepSeek-R1-Distill-Qwen-14B-FP8-dynamic

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8772|±  |0.0090|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8878|±  |0.0087|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2162|±  |0.0058|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2325|±  |0.0123|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1772|±  |0.0176|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.1983|±  |0.0182|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1451|±  |0.0117|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1722|±  |0.0163|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3364|±  |0.0160|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.1996|±  |0.0171|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5099|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5166|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2162|±  |0.0058|


#########################################################################

deepseek-ai/DeepSeek-R1-Distill-Qwen-14B

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8840|±  |0.0088|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8886|±  |0.0087|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2254|±  |0.0058|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2418|±  |0.0124|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1878|±  |0.0180|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2004|±  |0.0183|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1517|±  |0.0119|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1889|±  |0.0169|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3433|±  |0.0161|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2143|±  |0.0176|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5179|±  |0.0091|
|                                      |       |none            |    10|acc_norm   |↑  |0.5310|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2254|±  |0.0058|

#########################################################################

neuralmagic/DeepSeek-R1-Distill-Qwen-14B-quantized.w8a8

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8802|±  |0.0089|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8840|±  |0.0088|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2296|±  |0.0059|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2477|±  |0.0125|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1878|±  |0.0180|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2067|±  |0.0185|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1517|±  |0.0119|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1889|±  |0.0169|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3536|±  |0.0162|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2179|±  |0.0177|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5169|±  |0.0091|
|                                      |       |none            |    10|acc_norm   |↑  |0.5310|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2296|±  |0.0059|

#########################################################################

neuralmagic/DeepSeek-R1-Distill-Qwen-14B-quantized.w4a16

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0000|±  |0.0000|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8332|±  |0.0103|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8825|±  |0.0089|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.1898|±  |0.0055|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2056|±  |0.0117|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1456|±  |0.0162|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.1628|±  |0.0169|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1274|±  |0.0111|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1389|±  |0.0149|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3042|±  |0.0156|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.1886|±  |0.0168|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5146|±  |0.0091|
|                                      |       |none            |    10|acc_norm   |↑  |0.5229|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.1898|±  |0.0055|

##########################################################################

neody/r1-14b-awq

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8787|±  |0.0090|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8749|±  |0.0091|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2222|±  |0.0058|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2275|±  |0.0122|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1857|±  |0.0179|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2046|±  |0.0185|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1550|±  |0.0121|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1778|±  |0.0165|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3525|±  |0.0162|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2051|±  |0.0173|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5075|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5203|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2222|±  |0.0058|


##########################################################################

 --model vllm   --model_args pretrained=Jianyuan1/deepseek-r1-14b-cot-math-reasoning-full,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8886|±  |0.0087|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8840|±  |0.0088|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2286|±  |0.0059|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2393|±  |0.0124|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1941|±  |0.0182|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2046|±  |0.0185|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1595|±  |0.0122|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1981|±  |0.0172|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3444|±  |0.0161|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2161|±  |0.0176|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5162|±  |0.0091|
|                                      |       |none            |    10|acc_norm   |↑  |0.5286|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2286|±  |0.0059|

##########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/deepseek-14b-dyve-awq,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8787|±  |0.0090|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8741|±  |0.0091|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2146|±  |0.0057|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2190|±  |0.0120|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1878|±  |0.0180|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2046|±  |0.0185|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1429|±  |0.0117|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1630|±  |0.0159|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3433|±  |0.0161|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2015|±  |0.0172|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5069|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5199|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2146|±  |0.0057|


```



# gsm8k - LMDeploy Quants

```

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250 

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.848|±  |0.0228|
|     |       |strict-match    |     5|exact_match|↑  |0.844|±  |0.0230|


#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-mid,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250 

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.876|±  |0.0209|
|     |       |strict-match    |     5|exact_match|↑  |0.900|±  |0.0190|

#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.892|±  |0.0197|
|     |       |strict-match    |     5|exact_match|↑  |0.884|±  |0.0203|

#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max-max,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

vllm (pretrained=radna/r1-14b-awq-max-max,add_bos_token=True), gen_kwargs: (None), limit: 250.0, num_fewshot: 5, batch_size: auto
|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.860|±  |0.0220|
|     |       |strict-match    |     5|exact_match|↑  |0.856|±  |0.0222|


#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max-v2,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.892|±  |0.0197|
|     |       |strict-match    |     5|exact_match|↑  |0.884|±  |0.0203|


#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-mid-limo,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250

|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.904|±  |0.0187|
|     |       |strict-match    |     5|exact_match|↑  |0.880|±  |0.0206|


#########################################################################


lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max-pileval,add_bos_token=True   --tasks gsm8k  --num_fewshot 5 --batch_size auto --limit 250


|Tasks|Version|     Filter     |n-shot|  Metric   |   |Value|   |Stderr|
|-----|------:|----------------|-----:|-----------|---|----:|---|-----:|
|gsm8k|      3|flexible-extract|     5|exact_match|↑  |0.884|±  |0.0203|
|     |       |strict-match    |     5|exact_match|↑  |0.880|±  |0.0206|


```

# gsm8k,asdiv,hendrycks_math,mathqa - LMDeploy Quants

```

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8704|±  |0.0093|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8749|±  |0.0091|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.1586|±  |0.0051|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.1559|±  |0.0105|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1435|±  |0.0161|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.1524|±  |0.0164|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1107|±  |0.0104|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1148|±  |0.0137|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.2468|±  |0.0146|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.1648|±  |0.0159|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5106|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5173|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.1586|±  |0.0051|


#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-mid,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8317|±  |0.0103|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8787|±  |0.0090|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.1742|±  |0.0053|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.1702|±  |0.0109|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1414|±  |0.0160|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.1733|±  |0.0173|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1251|±  |0.0110|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1296|±  |0.0145|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.2675|±  |0.0150|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.1886|±  |0.0168|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5008|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5149|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.1742|±  |0.0053|

#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8772|±  |0.0090|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8681|±  |0.0093|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2298|±  |0.0059|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2334|±  |0.0123|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.2152|±  |0.0189|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2088|±  |0.0186|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1417|±  |0.0116|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1926|±  |0.0170|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3594|±  |0.0163|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2289|±  |0.0180|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5095|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5223|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2298|±  |0.0059|


#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max-max,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10


|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8764|±  |0.0091|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8757|±  |0.0091|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2166|±  |0.0058|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2207|±  |0.0120|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1730|±  |0.0174|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2171|±  |0.0189|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1440|±  |0.0117|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1759|±  |0.0164|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3364|±  |0.0160|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2143|±  |0.0176|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5146|±  |0.0091|
|                                      |       |none            |    10|acc_norm   |↑  |0.5276|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2166|±  |0.0058|


#########################################################################


lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max-v2,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8772|±  |0.0090|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8681|±  |0.0093|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2298|±  |0.0059|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2334|±  |0.0123|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.2152|±  |0.0189|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2088|±  |0.0186|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1417|±  |0.0116|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1926|±  |0.0170|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3594|±  |0.0163|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2289|±  |0.0180|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5095|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5223|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2298|±  |0.0059|


#########################################################################

lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-mid-limo,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10

|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8772|±  |0.0090|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8719|±  |0.0092|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2316|±  |0.0059|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2426|±  |0.0124|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1962|±  |0.0183|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2109|±  |0.0187|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1528|±  |0.0120|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1852|±  |0.0167|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3617|±  |0.0163|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2253|±  |0.0179|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5082|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5213|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2316|±  |0.0059|


#########################################################################


lm_eval   --model vllm   --model_args pretrained=radna/r1-14b-awq-max-pileval,add_bos_token=True   --tasks gsm8k,asdiv,hendrycks_math,mathqa  --batch_size auto --trust_remote_code --num_fewshot 10


|                Tasks                 |Version|     Filter     |n-shot|  Metric   |   |Value |   |Stderr|
|--------------------------------------|------:|----------------|-----:|-----------|---|-----:|---|-----:|
|asdiv                                 |      1|none            |    10|acc        |↑  |0.0004|±  |0.0004|
|gsm8k                                 |      3|flexible-extract|    10|exact_match|↑  |0.8802|±  |0.0089|
|                                      |       |strict-match    |    10|exact_match|↑  |0.8764|±  |0.0091|
|hendrycks_math                        |      1|none            |      |exact_match|↑  |0.2238|±  |0.0058|
| - hendrycks_math_algebra             |      1|none            |    10|exact_match|↑  |0.2233|±  |0.0121|
| - hendrycks_math_counting_and_prob   |      1|none            |    10|exact_match|↑  |0.1878|±  |0.0180|
| - hendrycks_math_geometry            |      1|none            |    10|exact_match|↑  |0.2025|±  |0.0184|
| - hendrycks_math_intermediate_algebra|      1|none            |    10|exact_match|↑  |0.1539|±  |0.0120|
| - hendrycks_math_num_theory          |      1|none            |    10|exact_match|↑  |0.1944|±  |0.0170|
| - hendrycks_math_prealgebra          |      1|none            |    10|exact_match|↑  |0.3548|±  |0.0162|
| - hendrycks_math_precalc             |      1|none            |    10|exact_match|↑  |0.2106|±  |0.0175|
|mathqa                                |      1|none            |    10|acc        |↑  |0.5102|±  |0.0092|
|                                      |       |none            |    10|acc_norm   |↑  |0.5199|±  |0.0091|

|    Groups    |Version|Filter|n-shot|  Metric   |   |Value |   |Stderr|
|--------------|------:|------|------|-----------|---|-----:|---|-----:|
|hendrycks_math|      1|none  |      |exact_match|↑  |0.2238|±  |0.0058|

```