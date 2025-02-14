
```
*Solve the provided math problem as follows:  
1. **Analyze the problem meticulously**, ensuring full understanding.  
2. **Use exact values only**—no approximations, estimations, or rounding at any stage.  
3. **Detail all steps** clearly in your reasoning process.  
4. **Verify each step rigorously** for accuracy before proceeding.  
5. **Compute the final answer modulo 1000** (i.e., remainder when divided by 1000).  
6. **Return the result** in LaTeX as `\boxed{answer}` **only if entirely confident**.  
If uncertainty arises or verification fails, do not submit an answer.*  

"Three airline companies operate flights from Dodola island. Each company has a different schedule of departures. The first company departs every 100 days, the second every 120 days and the third every 150 days. What is the greatest positive integer $d$ for which it is true that there will be $d$ consecutive days without a flight from Dodola island, regardless of the departure times of the various airlines?"

<think>
Alright, we have a math problem.

Hmm, it seems that I was asked to use exact numbers.

This means I should not be approximating calculations.

This means I should use fractions instead of decimals.

This means I should avoid cumbersome calculations.

Also, I should not submit answers that I am not sure.

I should not be submitting guesses.

```


```
thought_prefix_english = """<think>
Alright, we have a math problem.

Hmm, it seems that I was asked to use exact numbers.

This means I should not be approximating calculations.

This means I should use fractions instead of decimals.

This means I should avoid cumbersome calculations.

Also, I should not submit answers that I am not sure.

I should not be submitting guesses."""


though_prefix_chinese = """<think>
好的，我们有一个数学问题。

嗯，看来我被要求使用精确数字。

此外，对于我不确定的答案我不应该提交。"""


def create_starter_text(question: str, index: int) -> str:
    options = []
    for _ in range(1):
        messages = [
            {"role": "system", "content": "Solve the math problem from the user. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}."},
            {"role": "user", "content": question},
        ]
        starter_text = tokenizer.apply_chat_template(
            conversation=messages,
            tokenize=False,
            add_generation_prompt=True
        ) + thought_prefix_english
        options.append(starter_text)
    for _ in range(0):
        messages = [
            {"role": "system", "content": "请通过逐步推理来解答问题。只处理精确的数字。只有在确信无误时才提交答案。把最终答案对1000取余数，放置于\\boxed{}中。"},
            {"role": "user", "content": question},
        ]
        starter_text = tokenizer.apply_chat_template(
            conversation=messages,
            tokenize=False,
            add_generation_prompt=True
        ) + though_prefix_chinese
        options.append(starter_text)
    
    return options[index%len(options)]
```