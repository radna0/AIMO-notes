```
def create_starter_messages(question, index):
    options = []
    for _ in range(13):
        options.append(
            [
                {"role": "system", "content": "You are the most powerful math expert. Please solve the problems with deep resoning. You are careful and always recheck your conduction. You will never give answer directly until you have enough confidence. You should think step-by-step. Return final answer within \\boxed{}, after taking modulo 1000."},
                {"role": "user", "content": question},
            ]
        )
    for _ in range(2):    
        options.append(
            [
                {"role": "system", "content": "You are a helpful and harmless math assistant. You should think step-by-step and you are good at reverse thinking to recheck your answer and fix all possible mistakes. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}."},
                {"role": "user", "content": question},
            ],
        )
    options.append(
        [
            {"role": "system", "content": "Please carefully read the problem statement first to ensure you fully understand its meaning and key points. Then, solve the problem correctly and completely through deep reasoning. Finally, return the result modulo 1000 and enclose it in \\boxed{} like \"Atfer take the result modulo 1000, final anwer is \\boxed{180}."},
            {"role": "user", "content": question},
        ],
    )
    return options[index%len(options)]
```

