import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--max_tokens",
    type=int,
    default=1024 * 12,
    help="Maximum number of tokens to generate",
)
parser.add_argument(
    "--num_seqs",
    type=int,
    default=16,
    help="Number of sequences to generate per prompt",
)

args = parser.parse_args()


MODEL_NAME = "casperhansen/deepseek-r1-distill-qwen-14b-awq"
HF_TOKEN = "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"

EVAL_FILE = "hard_batch_1"
print(f"Using evaluation file: {EVAL_FILE}")


# copy file from ../data/aime/{EVAL_FILE}.csv to reference.csv
import shutil

shutil.copy(f"{EVAL_FILE}.csv", "reference.csv")


import os

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["VLLM_USE_V1"] = "1"

os.environ["VLLM_FLASH_ATTN_VERSION"] = "3"  # on h100 and above
# os.environ["VLLM_USE_TRITON_FLASH_ATTN"]='1'
# os.environ["VLLM_USE_TRITON_AWQ"]='1'

# os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER"
# os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "1"
# os.environ["VLLM_FLASHINFER_FORCE_TENSOR_CORES"] = "1"

# os.environ["VLLM_USE_RAY_SPMD_WORKER"]='1'
# os.environ["VLLM_ALLOW_LONG_MAX_MODEL_LEN"]='1'

import gc
import time
import warnings

import pandas as pd
import polars as pl
import numpy as np

import torch

pd.set_option("display.max_colwidth", None)
start_time = time.time()
cutoff_time = start_time + (4 * 60 + 55) * 60
cutoff_times = [int(x) for x in np.linspace(cutoff_time, start_time + 60 * 60, 50 + 1)]

from vllm import LLM, SamplingParams

warnings.simplefilter("ignore")

llm_model_pth = MODEL_NAME

# MAX_NUM_SEQS = 32
# MAX_MODEL_LEN = 8192

# BEST FOR 14B
MAX_NUM_SEQS = args.num_seqs
MAX_MODEL_LEN = args.max_tokens

# MAX_NUM_SEQS = 16
# MAX_MODEL_LEN = 1024 * 8

# MAX_NUM_SEQS = 24
# MAX_MODEL_LEN = 1024 * 8

# MAX_NUM_SEQS = 32
# MAX_MODEL_LEN = 8192 * 3 // 2

# BEST FOR 7B
# MAX_NUM_SEQS = 32
# MAX_MODEL_LEN = 1024 * 16

FINAL_EVAL_NAME = f"14B_AWQ_DeepSeek_{MAX_NUM_SEQS}x{MAX_MODEL_LEN}"

EVAL = True
EVAL_SELECTED_QUESTIONS_ONLY = False

llm = LLM(
    llm_model_pth,
    # dtype="half",                # The data type for the model weights and activations
    max_num_seqs=MAX_NUM_SEQS,  # Maximum number of sequences per iteration. Default is 256
    max_model_len=MAX_MODEL_LEN,  # Model context length
    trust_remote_code=True,  # Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer
    tensor_parallel_size=1,  # The number of GPUs to use for distributed execution with tensor parallelism
    gpu_memory_utilization=0.95,  # The ratio (between 0 and 1) of GPU memory to reserve for the model
    seed=2024,
    quantization="moe_wna16",
)

import vllm

print(vllm.__version__)

tokenizer = llm.get_tokenizer()

import re
import keyword


def extract_boxed_text(text):
    pattern = r"oxed{(.*?)}"
    matches = re.findall(pattern, text)
    if not matches:
        return ""
    for match in matches[::-1]:
        if match != "":
            return match
    return ""


from collections import Counter
import random


def select_answer(answers):
    counter = Counter()
    for answer in answers:
        try:
            if int(answer) == float(answer):
                counter[int(answer)] += 1 + random.random() / 1_000
        except:
            pass
    if not counter:
        return 210
    _, answer = sorted([(v, k) for k, v in counter.items()], reverse=True)[0]
    return answer % 1000


def batch_message_generate(list_of_messages) -> list[list[dict]]:
    max_tokens = MAX_MODEL_LEN
    if time.time() > cutoff_times[-1]:
        print("Speedrun")
        max_tokens = 1024 * 8

    sampling_params = SamplingParams(
        temperature=1.0,  # randomness of the sampling
        min_p=0.01,
        skip_special_tokens=True,  # Whether to skip special tokens in the output
        max_tokens=max_tokens,
        stop=["</think>"],
    )

    request_output = llm.generate(
        prompts=list_of_messages,
        sampling_params=sampling_params,
    )

    print(
        [
            len(single_request_output.outputs[0].token_ids)
            for single_request_output in request_output
        ]
    )

    sort_keys_and_list_of_messages = []

    for messages, single_request_output in zip(list_of_messages, request_output):
        # print()
        # print(single_request_output.outputs[0].text)
        # print()
        messages += single_request_output.outputs[0].text

        sort_keys_and_list_of_messages.append(
            (len(single_request_output.outputs[0].token_ids), messages)
        )

    print([sort_key for sort_key, _ in sort_keys_and_list_of_messages])
    sort_keys_and_list_of_messages.sort(
        key=lambda sort_key_and_messages: sort_key_and_messages[0]
    )
    print([sort_key for sort_key, _ in sort_keys_and_list_of_messages])

    list_of_messages = [messages for _, messages in sort_keys_and_list_of_messages]

    return list_of_messages


def create_starter_messages(question, index):
    options = []
    for _ in range(13):
        options.append(
            [
                {
                    "role": "system",
                    "content": "You are the most powerful math expert. Please solve the problems with deep resoning. You are careful and always recheck your conduction. You will never give answer directly until you have enough confidence. You should think step-by-step. Return final answer within \\boxed{}, after taking modulo 1000.",
                },
                {"role": "user", "content": question},
            ]
        )
    for _ in range(2):
        options.append(
            [
                {
                    "role": "system",
                    "content": "You are a helpful and harmless math assistant. You should think step-by-step and you are good at reverse thinking to recheck your answer and fix all possible mistakes. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.",
                },
                {"role": "user", "content": question},
            ],
        )

    options.append(
        [
            {
                "role": "system",
                "content": "Please carefully read the problem statement first to ensure you fully understand its meaning and key points. Then, solve the problem correctly and completely through deep reasoning. Finally, return the result modulo 1000 and enclose it in \\boxed{}.",
            },
            {"role": "user", "content": question},
        ],
    )

    starter_text = options[index % len(options)]

    res = tokenizer.apply_chat_template(
        conversation=starter_text, tokenize=False, add_generation_prompt=True
    )

    return res


def predict_for_question(question: str) -> int:
    import os
    import time

    start_time = time.time()

    if not EVAL and not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
        return 210

    if EVAL_SELECTED_QUESTIONS_ONLY and not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
        # if "Triangle" not in question:
        #     return 210
        if (
            "Triangle" not in question
            and "delightful" not in question
            and "George" not in question
        ):
            return 210

    if time.time() > cutoff_time:
        return 210

    print(question)

    num_seqs = MAX_NUM_SEQS
    if time.time() > cutoff_times[-1]:
        num_seqs = 16

    list_of_messages = [
        create_starter_messages(question, index) for index in range(num_seqs)
    ]
    list_of_messages = batch_message_generate(list_of_messages)

    if not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
        df = pd.DataFrame(
            {
                "question": [question] * len(list_of_messages),
                "message": [messages for messages in list_of_messages],
            }
        )
        df.to_csv(f"{str(int(time.time() - start_time)).zfill(5)}.csv", index=False)

    all_extracted_answers = [
        extract_boxed_text(completion_text) for completion_text in list_of_messages
    ]

    print(all_extracted_answers)
    answer = select_answer(all_extracted_answers)
    print(answer)

    print("\n\n")
    print(f"Time taken: {time.time() - start_time}")
    cutoff_times.pop()
    return answer


# Replace this function with your inference code.
# The function should return a single integer between 0 and 999, inclusive.
# Each prediction (except the very first) must be returned within 30 minutes of the question being provided.

# Path to the temporary CSV file
import uuid

uid = str(uuid.uuid4())


TEMP_CSV = f"evals_{uid}_{EVAL_FILE}.csv"


def predict(id_: pl.DataFrame, question: pl.DataFrame) -> pl.DataFrame | pd.DataFrame:
    id_ = id_["id"][0]
    print("------")
    print(id_)

    question = question["problem"][0]
    answer = predict_for_question(question)
    print(question)
    print("------\n\n\n")

    if EVAL and not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
        # Prepare a row to log (you can add more columns if needed)
        row = {"id": id_, "question": question, "answer": answer}

        # Create a temporary DataFrame for this single prediction
        temp_df = pd.DataFrame([row])

        # If the CSV file doesn't exist, write with headers;
        # otherwise, append without writing the header.
        if not os.path.exists(TEMP_CSV):
            temp_df.to_csv(TEMP_CSV, index=False)
        else:
            temp_df.to_csv(TEMP_CSV, mode="a", header=False, index=False)

    return pl.DataFrame({"id": id_, "answer": answer})


""" predict_for_question(
    "Fred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements.)"
)
predict_for_question(
    "Triangle $ABC$ has side length $AB = 120$ and circumradius $R = 100$. Let $D$ be the foot of the perpendicular from $C$ to the line $AB$. What is the greatest possible length of segment $CD$?"
)
"""

pd.read_csv("reference.csv").drop("answer", axis=1).to_csv(
    "pure_reference.csv", index=False
)


def sample_and_predict(csv_file: str) -> None:
    """
    Reads all rows from the given CSV file, and for each row,
    calls the predict() function to process the problem.
    """
    # Attempt to read the CSV file.
    df = pd.read_csv(csv_file)

    # randomly shuffle the rows
    df = df.sample(frac=1, random_state=2024).reset_index(drop=True)

    # Loop through every row in the DataFrame.
    for index, row in df.iterrows():
        id_value = row["id"]
        problem_value = row["problem"]

        print(f"Processing row {index}: id = {id_value}, problem = {problem_value}")

        # Convert the values to single-row polars DataFrames.
        id_df = pl.DataFrame({"id": [id_value]})
        problem_df = pl.DataFrame({"problem": [problem_value]})

        # Call the predict function.
        result = predict(id_df, problem_df)
        print("Prediction result:")
        print(result)
        print("\n")
        # Optionally add a small delay if needed.
        # time.sleep(1)


sample_and_predict("pure_reference.csv")

# if EVAL and not EVAL_SELECTED_QUESTIONS_ONLY and not os.getenv('KAGGLE_IS_COMPETITION_RERUN'):
if (
    EVAL
    and not EVAL_SELECTED_QUESTIONS_ONLY
    and not os.getenv("KAGGLE_IS_COMPETITION_RERUN")
):
    import pandas as pd

    # File paths (adjust if needed)
    reference_input_path = "reference.csv"
    predictions_path = TEMP_CSV

    # Load the CSV files
    reference_df = pd.read_csv(reference_input_path)
    predictions_df = pd.read_csv(predictions_path)

    # Ensure the 'id' columns are strings and strip any extra whitespace
    reference_df["id"] = reference_df["id"].astype(str).str.strip()
    predictions_df["id"] = predictions_df["id"].astype(str).str.strip()

    # Optionally, normalize the answer columns (e.g., lowercasing and stripping whitespace)
    reference_df["answer"] = reference_df["answer"].astype(str).str.strip().str.lower()
    predictions_df["answer"] = (
        predictions_df["answer"].astype(str).str.strip().str.lower()
    )

    # Merge the predictions with the reference data on the common 'id' column.
    merged_df = pd.merge(
        reference_df,
        predictions_df,
        on="id",
        how="inner",
        suffixes=("_ref", "_pred"),
    )

    # Compare the answers. (Adjust this comparison if your answers require special handling.)
    merged_df["is_correct"] = merged_df["answer_ref"] == merged_df["answer_pred"]

    # Calculate metrics
    total = len(merged_df)
    correct = merged_df["is_correct"].sum()
    accuracy = correct / total

    print(f"Total predictions compared: {total}")
    print(f"Number of correct predictions: {correct}")
    print(f"Accuracy: {accuracy:.2%}")

    # Optionally, list the rows where the prediction did not match the reference.
    incorrect_df = merged_df[~merged_df["is_correct"]]
    if not incorrect_df.empty:
        print("\nIncorrect predictions:")
        # Adjust the columns below if your CSVs have different column names.
        print(incorrect_df[["id", "problem", "answer_ref", "answer_pred"]])
    else:
        print("\nAll predictions match the reference!")
