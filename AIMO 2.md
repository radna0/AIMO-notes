```

-** Select 2 Best Submission at the end

- To get 47/50 on both public and private test set
=> Model needs to handle variants really well
=> GSM Symbolic + RL + 

For 47/50 score, reference score needs to be:
- 47/50 => 94/100 => 94% correct
- 10 runs on 10 reference problems
- 4/10 runs needs to be 100% or 10/10
- 6/10 runs needs to be 90% or 9/10



# AWQ DeepSeek-R1-Distill-Qwen-14B
################################### BEST #######
MAX_NUM_SEQS = 16
MAX_MODEL_LEN = 8192 * 3 // 2

Total predictions compared: 10
Number of correct predictions: 7
Accuracy: 70.00%
-* moe_wna16 enabled from 6.5 -> 5.5

(8.2 + 5.5 + 7.4 + 8.5 + 8.5 + 5.5 + 8.5 + 5.5 + 8.5 + 8.5) / 10 = 7.5/problem

###################################
MAX_NUM_SEQS = 12
MAX_MODEL_LEN = 8192 * 3 // 2


Total predictions compared: 10
Number of correct predictions: 5
Accuracy: 50.00%

(5.1 + 7.4 + 7.3 + 5 + 7.1 + 7.4 + 5 + 7.2 + 7.3 + 5.2) /10 = 6.4/problem


############################################################ MID BEST #######
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192


Total predictions compared: 10
Number of correct predictions: 7
Accuracy: 70.00%

(6.5 + 7.5 + 6.3 + 7.3 + 7.2 + 7.3  + 7.3 + 6.0 + 6.1 + 7.1) /10 = 6.8/ problem

################################################################
MAX_NUM_SEQS = 24
MAX_MODEL_LEN = 10 * 1024

################################################################
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192 * 3 // 2

Total predictions compared: 10
Number of correct predictions: 7
Accuracy: 70.00%

 => ########## STUCK BECAUSE OF AI HARD QUESTIONS 







# AWQ DeepSeek-R1-Distill-Qwen-7B
################################################################ CUR BEST #######
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 8192 * 3 // 2


################################################################
MAX_NUM_SEQS = 32
MAX_MODEL_LEN = 15 * 1024



-gpu-memory utilization 0.96 vs 0.95

```
