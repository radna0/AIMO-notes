import os
import modal
import subprocess

import random

id = random.randint(0, 1000000)

cuda_version = "12.4.0"  # should be no greater than host CUDA version
flavor = "devel"  #  includes full CUDA toolkit
operating_sys = "ubuntu22.04"
tag = f"{cuda_version}-{flavor}-{operating_sys}"

app = modal.App(f"eval-{id}-notebook")


N_GPU = 1  # tip: for best results, first upgrade to more powerful GPUs, and only then increase GPU count

MINUTES = 60  # seconds
HOURS = 60 * MINUTES


# MODEL_NAME = "casperhansen/deepseek-r1-distill-qwen-14b-awq"

# Modified Version of AWQ
# MODEL_NAME = "radna/deepseek-r1-distill-qwen-7b-awq"

MODEL_NAME = "radna/deepseek-14b-dyve-awq-triton"
HF_TOKEN = "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"


# VERY SLOW
# MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

# take in args

EVAL_FILE = "reference"
print(f"Using evaluation file: {EVAL_FILE}")


def hf_download():
    from huggingface_hub import hf_hub_download, snapshot_download

    deepseek_model = snapshot_download(
        MODEL_NAME,
        cache_dir="/cache",
        token=HF_TOKEN,
        force_download=True,
    )


vol = modal.Volume.from_name(
    "hf-hub-cache",
    create_if_missing=True,
)


vllm_image = (
    modal.Image.from_registry(f"nvidia/cuda:{tag}", add_python="3.12")
    .apt_install("git", "build-essential", "cmake", "curl", "libcurl4-openssl-dev")
    .pip_install(
        "lmdeploy",
        "torch",
        "transformers",
        "pandas",
        "polars",
        "numpy",
        "huggingface_hub[hf_transfer]",
        "flashinfer-python",
    )
    .env({"HF_HUB_ENABLE_HF_TRANSFER": "0"})
    .run_function(
        hf_download,
        # persist the HF cache to a Modal Volume so future runs don't re-download models
        volumes={"/cache": vol},
    )
    .run_commands(
        f"huggingface-cli login --token {HF_TOKEN}",
    )
    .add_local_file(f"data/aime/{EVAL_FILE}.csv", remote_path="/root/reference.csv")
)


@app.function(
    image=vllm_image,
    gpu=modal.gpu.H100(count=N_GPU),
    container_idle_timeout=5 * MINUTES,
    timeout=24 * HOURS,
    # allow_concurrent_inputs=1000,
)
def eval():
    import os

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["VLLM_USE_V1"] = "1"

    os.environ["VLLM_FLASH_ATTN_VERSION"] = "3"  # on h100 and above
    import gc
    import time
    import warnings

    import pandas as pd
    import polars as pl
    import numpy as np

    import torch

    pd.set_option("display.max_colwidth", None)
    start_time = time.time()
    cutoff_time = start_time + (1 * 60 + 55) * 60
    cutoff_times = [
        int(x) for x in np.linspace(cutoff_time, start_time + 20 * 60, 50 + 1)
    ]

    warnings.simplefilter("ignore")

    llm_model_pth = MODEL_NAME

    MAX_NUM_SEQS = 32
    MAX_MODEL_LEN = 1024 * 12

    FINAL_EVAL_NAME = f"7B_AWQ_DeepSeek_{MAX_NUM_SEQS}x{MAX_MODEL_LEN}"

    EVAL = True
    EVAL_SELECTED_QUESTIONS_ONLY = False

    import re

    def extract_boxed_text(text: str) -> str:
        pattern: str = r"oxed{(.*?)}"
        matches: list[str] = re.findall(pattern, text)
        if not matches:
            return ""
        for match in matches[::-1]:
            if match != "":
                return match
        return ""

    from collections import defaultdict
    import random

    def select_answer(answers: list[str]) -> int:
        counter: defaultdict[int, float] = defaultdict(float)
        for answer in answers:
            try:
                if int(answer) == float(answer):
                    counter[int(answer)] += (1 + random.random() / 1_000) * 1_000_000
            except Exception:
                pass
        if not counter:
            return -1
        _, answer_result = sorted([(v, k) for k, v in counter.items()], reverse=True)[0]
        return answer_result % 1000

    from lmdeploy import pipeline, TurbomindEngineConfig, GenerationConfig

    engine_config = TurbomindEngineConfig(
        quant_policy=4,
        max_batch_size=MAX_NUM_SEQS,
        enable_prefix_caching=True,
        cache_max_entry_count=0.8,
        session_len=MAX_MODEL_LEN,
    )
    gen_config = GenerationConfig(
        temperature=0.6,  # randomness of the sampling
        min_p=0.01,
        max_new_tokens=MAX_MODEL_LEN - 200,
        do_sample=True,
        skip_special_tokens=True,
        stop_words=["</think>"],
    )
    pipe = pipeline(MODEL_NAME, backend_config=engine_config)

    start = time.time()
    response = pipe(
        [
            "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.\nTriangle $ABC$ has side length $AB = 120$ and circumradius $R = 100$. Let $D$ be the foot of the perpendicular from $C$ to the line $AB$. What is the greatest possible length of segment $CD$?"
            for _ in range(MAX_NUM_SEQS)
        ],
        gen_config=gen_config,
    )
    print(f"Time Taken: {time.time() - start}")
    print(response[0])
    print(len(response))
    answers = [extract_boxed_text(res.text) for res in response]
    print(answers)
    print(select_answer(answers))

    start = time.time()
    response = pipe(
        [
            "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.\nFred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements.)"
            for _ in range(MAX_NUM_SEQS)
        ],
        gen_config=gen_config,
    )
    """ response = pipe(
        [
            "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.\nFred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements.)"
            for _ in range(MAX_NUM_SEQS)
        ],
        gen_config=gen_config,
    ) """
    print(f"Time Taken: {time.time() - start}")
    print(len(response))
    answers = [extract_boxed_text(res.text) for res in response]
    print(answers)
    print(select_answer(answers))

    start = time.time()
    response = pipe(
        [
            "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.\nWe call a sequence $a_1, a_2, \\ldots$ of non-negative integers \\textit{delightful} if there exists a positive integer $N$ such that for all $n > N$, $a_n = 0$, and for all $i \\geq 1$, $a_i$ counts the number of multiples of $i$ in $a_1, a_2, \\l\\dots, a_N$. How many delightful sequences of non-negative integers are there?"
            for _ in range(MAX_NUM_SEQS)
        ],
        gen_config=gen_config,
    )
    print(f"Time Taken: {time.time() - start}")
    print(len(response))
    answers = [extract_boxed_text(res.text) for res in response]
    print(answers)
    print(select_answer(answers))

    start = time.time()
    response = pipe(
        [
            "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.\nThree airline companies operate flights from Dodola island. Each company has a different schedule of departures. The first company departs every 100 days, the second every 120 days and the third every 150 days. What is the greatest positive integer $d$ for which it is true that there will be $d$ consecutive days without a flight from Dodola island, regardless of the departure times of the various airlines?"
            for _ in range(MAX_NUM_SEQS)
        ],
        gen_config=gen_config,
    )
    print(f"Time Taken: {time.time() - start}")
    print(len(response))
    answers = [extract_boxed_text(res.text) for res in response]
    print(answers)
    print(select_answer(answers))


@app.local_entrypoint()
def main():
    eval.remote()
