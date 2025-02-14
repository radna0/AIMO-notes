import os
import requests
import time
import multiprocessing
import re
import pandas as pd
import random

OVH_AI_ENDPOINTS_ACCESS_TOKEN = "64MA63E3RORIU6SSLWYTULFH2R66JAHEXIUQ"

df = pd.read_csv("../data/aimo_2025_I.csv")

question = random.choice(df["problem"].dropna().tolist())
print(question)


def extract_boxed_text(text):
    pattern = r"oxed{(.*?)}"
    matches = re.findall(pattern, text)
    if not matches:
        return ""
    for match in matches[::-1]:
        if match != "":
            return match
    return ""


def api_call_process():
    start = time.time()
    res = False
    while not res:
        try:
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
                response_data = response.json()
                choices = response_data.get("choices", [])
                for choice in choices:
                    text = choice.get("message", {}).get("content", "")
                    boxed_text = extract_boxed_text(text)
                    print(f"Boxed text answer: {boxed_text}")
                    res = True
            else:
                raise Exception(f"API call failed - Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

    end = time.time()
    print(f"Process time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main_start = time.time()
    processes = []
    sleep_time = 5
    for _ in range(4):
        p = multiprocessing.Process(target=api_call_process)
        processes.append(p)
        p.start()
        time.sleep(sleep_time)

    for p in processes:
        p.join()

    main_end = time.time()
    print(f"Total time taken: {main_end - main_start:.2f} seconds")
