
```
# AWQ DeepSeek-R1-Distill-Qwen-14B
############### BAD
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192


Total predictions compared: 30
Number of correct predictions: 20
Accuracy: 66.67%

Wrongs:
    61,
    62,
    63,
    73,
    74,
    76,
    80,
    81,
    88,
    89,

################################### MID
MAX_NUM_SEQS = 24
MAX_MODEL_LEN = 10 * 1024

Total predictions compared: 30
Number of correct predictions: 24
Accuracy: 80.00%

Incorrect predictions:
    id  ... answer_pred
2   62  ...         210
3   63  ...         210
13  73  ...         254
21  81  ...         210
28  88  ...         210
29  89  ...         210


##############################################  BEST
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192 * 3 // 2

Total predictions compared: 30
Number of correct predictions: 24
Accuracy: 80.00%

Incorrect predictions:
    id  ... answer_pred
2   62  ...         145
3   63  ...          16
13  73  ...         287
21  81  ...         210
28  88  ...         210
29  89  ...          24


##############################################  Got Lucky???
MAX_NUM_SEQS = 12
MAX_MODEL_LEN = 8192 * 3 // 2

Total predictions compared: 30
Number of correct predictions: 24
Accuracy: 80.00%

Incorrect predictions:
    id  ... answer_pred
2   62  ...         210
3   63  ...          48
4   64  ...         155
21  81  ...           9
28  88  ...         210
29  89  ...          49
  


############################################## Testing Only
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192 * 3 // 2

Total predictions compared: 30
Number of correct predictions: 24
Accuracy: 80.00%

Incorrect predictions:
    id  ... answer_pred
2   62  ...         145
3   63  ...          24
13  73  ...         603
21  81  ...          22
28  88  ...           7
29  89  ...          24


```

```

# AWQ DeepSeek-R1-Distill-Qwen-7B
############################################## Stable?
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 16

otal predictions compared: 30
Number of correct predictions: 22
Accuracy: 73.33%

Incorrect predictions:
    id  ... answer_pred
2   62  ...         311
3   63  ...          16
4   64  ...         155
13  73  ...         273
21  81  ...          24
25  85  ...         100
28  88  ...           7
29  89  ...          24

  
############################################## UnStable?
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192 * 3 // 2

Total predictions compared: 30
Number of correct predictions: 22
Accuracy: 73.33%

Incorrect predictions:
    id  ... answer_pred
2   62  ...          39
3   63  ...           4
4   64  ...         155
13  73  ...         254
21  81  ...          36
25  85  ...         100
28  88  ...         210
29  89  ...          24



```


# LIMO AIME Evals - PEP = PURE ENGLISH


```
# NON-AWQ OpenR1-Qwen-7B
##############################################  
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 16


Total predictions compared: 30
Number of correct predictions: 21
Accuracy: 70.00%

Incorrect predictions:
    id  ... answer_pred
2   62  ...          75
3   63  ...          16
13  73  ...         254
17  77  ...          13
20  80  ...          17
21  81  ...          54
25  85  ...         100
28  88  ...           9
29  89  ...           2

##############################################  
MAX_NUM_SEQS = 48
MAX_MODEL_LEN = 1024 * 16

Total predictions compared: 30
Number of correct predictions: 22
Accuracy: 73.33%

Incorrect predictions:
    id  ... answer_pred
2   62  ...         419
3   63  ...          16
4   64  ...         155
13  73  ...          36
17  77  ...          13
21  81  ...          54
25  85  ...         240
29  89  ...           2


##############################################  
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 32

Total predictions compared: 30
Number of correct predictions: 22
Accuracy: 73.33%

Incorrect predictions:
    id  ... answer_pred
2   62  ...         383
3   63  ...          16
13  73  ...         103
18  78  ...          19
21  81  ...          54
25  85  ...         100
28  88  ...          10
29  89  ...          24

```


```
# NON-AWQ DeepSeek-Qwen-1.5B
##############################################  
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 1024 * 24


Total predictions compared: 30
Number of correct predictions: 14
Accuracy: 46.67%

Incorrect predictions:
    id  ... answer_pred
1   61  ...          11
2   62  ...          73
3   63  ...          16
4   64  ...         155
5   65  ...          52
10  70  ...         107
13  73  ...          35
14  74  ...          80
15  75  ...         229
17  77  ...           0
20  80  ...          13
21  81  ...          12
25  85  ...          40
27  87  ...          16
28  88  ...           6
29  89  ...           2
```