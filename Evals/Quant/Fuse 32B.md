

```

python eval_lmdeploy.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ  --file aime_2025.csv --num_seqs 5 --tokens 12288 --quant_policy 8 --min_p 0.10 --top_k 50 > evals.log 2>&1 &

Total predictions compared: 60
Number of correct predictions: 18
Accuracy: 30.00%


Time Taken: 3234.5514822006226

python eval_lmdeploy.py --model Valdemardi/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview-AWQ  --file aime_2025.csv --num_seqs 5 --tokens 12288 --quant_policy 0 --min_p 0.10 --top_k 0 > evals.log 2>&1 &


19/30


Total predictions compared: 60
Number of correct predictions: 19
Accuracy: 31.67%
Time Taken: 3519.461321115494

```