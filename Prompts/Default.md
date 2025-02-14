```
def create_starter_messages(question, index):
    options = []
    for _ in range(13):
        options.append(
            [
                {"role": "system", "content": "You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}, after taking modulo 1000."},
                {"role": "user", "content": question},
            ]
        )
    for _ in range(2):    
        options.append(
            [
                {"role": "system", "content": "You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}."},
                {"role": "user", "content": question},
            ],
        )
    options.append(
        [
            {"role": "system", "content": "请通过逐步推理来解答问题，并把最终答案对1000取余数，放置于\\boxed{}中。"},
            {"role": "user", "content": question},
        ],
    )
    return options[index%len(options)]
```
