OVH_AI_ENDPOINTS_ACCESS_TOKEN = "64MA63E3RORIU6SSLWYTULFH2R66JAHEXIUQ"


import os
import requests
import time

start = time.time()

question = "Find the sum of all integer bases $b>9$ for which $17_{b}$ is a divisor of $97_{b}$"

url = "https://api.vultrinference.com/v1/chat/completions"
payload = {
    "model": "deepseek-r1-distill-qwen-32b",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful and harmless math assistant. You should think step-by-step and you are good at reverse thinking to recheck your answer and fix all possible mistakes. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.",
        },
        {
            "role": "user",
            "content": question,
        },
    ],
    "max_tokens": 1024 * 8,
    "temperature": 0,
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OVH_AI_ENDPOINTS_ACCESS_TOKEN}",
}

response = requests.post(url, json=payload, headers=headers)
if response.status_code == 200:
    # Handle response
    response_data = response.json()
    # Parse JSON response
    choices = response_data["choices"]
    for choice in choices:
        text = choice["message"]["content"]
        # Process text and finish_reason
        print(text)
else:
    print("Error:", response.status_code)

end = time.time()
print(f"Time taken: {end - start:.2f} seconds")
