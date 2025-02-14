# DEFAULT MIXED PROMPT
```
# AWQ DeepSeek-R1-Distill-Qwen-14B
############################################## BEST??
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192 * 3 // 2


Total predictions compared: 15
Number of correct predictions: 7
Accuracy: 46.67%

Incorrect predictions:
    id  ... answer_pred
1    7  ...         271
2    8  ...           8
3    10  ...        210
4    11  ...        210
5    12  ...        679
6    13  ...        179
7    14  ...        210
8    15  ...        147

############################################## TESTING
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192 * 3 // 2

Total predictions compared: 15
Number of correct predictions: 9
Accuracy: 60.00%

Incorrect predictions:
    id  ... answer_pred
6    7  ...         271
9   10  ...          29
10  11  ...           0
12  13  ...         129
13  14  ...         115
14  15  ...         147


```



```

# AWQ DeepSeek-R1-Distill-Qwen-7B
############################################## BETTER BEST?
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 16

Total predictions compared: 15
Number of correct predictions: 8
Accuracy: 53.33%

Incorrect predictions:
    id  ... answer_pred
6    7  ...          12
9   10  ...         210
10  11  ...           2
11  12  ...         508
12  13  ...         129
13  14  ...          63
14  15  ...         147

  
############################################## TESTING?
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 32

Total predictions compared: 15
Number of correct predictions: 9
Accuracy: 60.00%

Incorrect predictions:
    id  ... answer_pred
6    7  ...          12
9   10  ...         210
10  11  ...           1
12  13  ...         129
13  14  ...          42
14  15  ...         147


```



# PEP = PURE ENGLISH PROMPT


```
# AWQ DeepSeek-R1-Distill-Qwen-14B
##############################################  TESTING ONLY
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 16


Total predictions compared: 15
Number of correct predictions: 9
Accuracy: 60.00%

Incorrect predictions:
    id  ... answer_pred
6    7  ...         311
9   10  ...         210
10  11  ...           0
12  13  ...         210
13  14  ...          81
14  15  ...         147

##############################################  CUR BEST
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192 * 3 // 2



```


```

# AWQ DeepSeek-R1-Distill-Qwen-7B
############################################## BETTER BEST?
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 16


######################## TEST 1
Total predictions compared: 15
Number of correct predictions: 8
Accuracy: 53.33%

Incorrect predictions:
    id  ... answer_pred
6    7  ...          12
9   10  ...          24
10  11  ...          43
11  12  ...         508
12  13  ...         129
13  14  ...          87
14  15  ...         147

######################## TEST 2
Total predictions compared: 15
Number of correct predictions: 9
Accuracy: 60.00%

Incorrect predictions:
    id  ... answer_pred
6    7  ...          12
9   10  ...         134
10  11  ...           0
12  13  ...         126
13  14  ...          68
14  15  ...         147

######################## TEST 3
Total predictions compared: 15
Number of correct predictions: 9
Accuracy: 60.00%

Incorrect predictions:
    id  ... answer_pred
6    7  ...          12
9   10  ...          91
10  11  ...           5
12  13  ...         129
13  14  ...          76
14  15  ...         147

```



```
# NON-AWQ OpenR1-Qwen-7B
############################################## CRAZY GOOD!!!
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 16

Total predictions compared: 15
Number of correct predictions: 9
Accuracy: 60.00%

Incorrect predictions:
    id  ... answer_pred
6    7  ...           0
9   10  ...          96
10  11  ...         161
12  13  ...         129
13  14  ...          47
14  15  ...         147


Total predictions compared: 15
Number of correct predictions: 8
Accuracy: 53.33%

Incorrect predictions:
    id  ... answer_pred
6    7  ...          12
9   10  ...          96
10  11  ...         264
11  12  ...          16
12  13  ...         129
13  14  ...          73
14  15  ...         147

Total predictions compared: 15
Number of correct predictions: 9
Accuracy: 60.00%

Incorrect predictions:
    id  ... answer_pred
6    7  ...           6
9   10  ...          96
10  11  ...         210
12  13  ...         145
13  14  ...          49
14  15  ...         147


# AWQ VERSION NEEDED

```


```
# NON-AWQ DeepSeek-Qwen-1.5B
##############################################  
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 24

Total predictions compared: 15
Number of correct predictions: 6
Accuracy: 40.00%

Incorrect predictions:
    id  ... answer_pred
4    5  ...         975
6    7  ...          12
8    9  ...           6
9   10  ...          13
10  11  ...           0
11  12  ...          16
12  13  ...         126
13  14  ...          91
14  15  ...         147

```