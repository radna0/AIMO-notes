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

# NON-AWQ BUT Still Very Fast
# MODEL_NAME = "radna/OpenR1-Qwen-7B-AWQ"
MODEL_NAME = "casperhansen/deepseek-r1-distill-qwen-14b-awq"
HF_TOKEN = "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"


# VERY SLOW
# MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"

# take in args

EVAL_FILE = "hard_batch_1"
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
        "vllm==0.7.2",
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
        "git clone https://github.com/radna0/Dynasor.git",
        "cd Dynasor && pip install . && cd -",
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
    # cutoff_time = start_time + (4 * 60 + 45) * 60
    # cutoff_times = [
    #     int(x) for x in np.linspace(cutoff_time, start_time + 60 * 60, 50 + 1)
    # ]

    from vllm import LLM, SamplingParams

    warnings.simplefilter("ignore")

    llm_model_pth = MODEL_NAME

    # MAX_NUM_SEQS = 32
    # MAX_MODEL_LEN = 8192

    # BEST FOR 14B
    # MAX_NUM_SEQS = 16
    # MAX_MODEL_LEN = 8192 * 3 // 2

    MAX_NUM_SEQS = 16
    MAX_MODEL_LEN = 1024 * 12

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

    from dynasor.core.entropy import (
        should_early_exit,
        uncertain_words,
        is_certain_answer,
    )

    probe_text = "... Oh, I suddenly got the answer to the whole problem, **Final Answer**\n\n\\[ \\boxed{"
    probe_text_end = "}"
    certainty_window = 2
    token_interval = 32

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
        """Weight answers from later stages more heavily"""
        weighted_answers = []
        for i, ans in enumerate(answers):
            try:
                num = int(float(ans))
                # Exponential weighting based on position
                weight = 1.5**i
                weighted_answers.extend([num] * int(weight))
            except:
                continue

        if not weighted_answers:
            return 210

        counter = Counter(weighted_answers)
        return max(counter.items(), key=lambda x: x[1])[0] % 1000

    def batch_message_generate(list_of_messages) -> list[list[dict]]:
        max_tokens = MAX_MODEL_LEN
        token_budgets = [max_tokens] * len(
            list_of_messages
        )  # Track remaining tokens per sequence
        answers_history = [[] for _ in list_of_messages]
        certainties_history = [[] for _ in list_of_messages]
        active_indices = list(range(len(list_of_messages)))

        # Initial generation parameters
        sampling_params = SamplingParams(
            temperature=1.0,
            min_p=0.01,
            skip_special_tokens=True,
            max_tokens=min(token_interval, max_tokens),  # Initial chunk size
            stop=["</think>"],
        )

        while active_indices:
            # Generate next chunk
            current_prompts = [list_of_messages[i] for i in active_indices]
            request_output = llm.generate(current_prompts, sampling_params)

            # Process outputs and probe
            new_active = []
            probe_prompts = []
            probe_indices = []

            for idx, output in zip(active_indices, request_output):
                # Update token budget
                generated_tokens = len(output.outputs[0].token_ids)
                token_budgets[idx] -= generated_tokens

                # Stop sequences that exceed budget
                if token_budgets[idx] <= 0:
                    continue

                # Update message with generated text
                list_of_messages[idx] += output.outputs[0].text

                # Prepare probing
                probe_prompt = list_of_messages[idx] + probe_text
                probe_prompts.append(probe_prompt)
                probe_indices.append(idx)

            # Get probe responses
            if probe_prompts:
                probe_params = SamplingParams(
                    temperature=0.6, top_p=0.95, max_tokens=20, skip_special_tokens=True
                )
                probe_outputs = llm.generate(probe_prompts, probe_params)

                for idx, probe_out in zip(probe_indices, probe_outputs):
                    # Update probe token budget
                    probe_tokens = len(probe_out.outputs[0].token_ids)
                    token_budgets[idx] -= probe_tokens

                    # Process probe response
                    probe_response_text = probe_out.outputs[0].text
                    answer = extract_boxed_text(probe_response_text)
                    certain = is_certain_answer(probe_response_text, uncertain_words)

                    answers_history[idx].append(answer)
                    certainties_history[idx].append(certain)

                    if should_early_exit(
                        answers_history[idx],
                        probe_response_text,
                        uncertain_words,
                        certainty_window,
                        certainties_history[idx],
                    ):
                        # Finalize answer
                        list_of_messages[idx] += f"{probe_text}{answer}{probe_text_end}"
                        print(
                            f"Early Exit with message: Length={len(list_of_messages[idx])} - Probe='{probe_text}{answer}{probe_text_end}'"
                        )
                    else:
                        new_active.append(idx)

            # Update active indices and chunk size
            active_indices = new_active
            remaining_budgets = [token_budgets[i] for i in active_indices]

            if remaining_budgets:
                sampling_params.max_tokens = min(
                    token_interval,
                    min(remaining_budgets),  # Don't exceed smallest remaining budget
                )

        # Sort by final sequence length
        sorted_outputs = sorted(
            [(len(msg), msg) for msg in list_of_messages],
            key=lambda x: x[0],
            reverse=True,
        )
        return [msg for _, msg in sorted_outputs]

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

        if EVAL_SELECTED_QUESTIONS_ONLY and not os.getenv(
            "KAGGLE_IS_COMPETITION_RERUN"
        ):
            # if "Triangle" not in question:
            #     return 210
            if (
                "Triangle" not in question
                and "delightful" not in question
                and "George" not in question
            ):
                return 210

        # if time.time() > cutoff_time:
        #     return 210

        print(question)

        num_seqs = MAX_NUM_SEQS
        # if time.time() > cutoff_times[-1]:
        #     num_seqs = 2 * MAX_NUM_SEQS // 3

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
        # cutoff_times.pop()
        return answer

    # Replace this function with your inference code.
    # The function should return a single integer between 0 and 999, inclusive.
    # Each prediction (except the very first) must be returned within 30 minutes of the question being provided.

    # Path to the temporary CSV file
    TEMP_CSV = f"evals_reference_{EVAL_FILE}.csv"

    def predict(
        id_: pl.DataFrame, question: pl.DataFrame
    ) -> pl.DataFrame | pd.DataFrame:
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
        "Fred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \textit{different} if there is a player with a different opponent in the two arrangements.)"
    ) """
    predict_for_question(
        "Fred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements.)"
    )
    predict_for_question(
        "Triangle $ABC$ has side length $AB = 120$ and circumradius $R = 100$. Let $D$ be the foot of the perpendicular from $C$ to the line $AB$. What is the greatest possible length of segment $CD$?"
    )

    return

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
        reference_df["answer"] = (
            reference_df["answer"].astype(str).str.strip().str.lower()
        )
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

        import io

        evals_csv_buffer = io.StringIO()
        predictions_df.to_csv(evals_csv_buffer, index=False)
        csv_content = evals_csv_buffer.getvalue()
        return csv_content.encode("utf-8"), FINAL_EVAL_NAME


EVALS_DIR = "evals/"


@app.local_entrypoint()
def main():
    os.makedirs(EVALS_DIR, exist_ok=True)
    data, file_postfix = eval.remote()
    filename = os.path.join(EVALS_DIR, f"aime_{EVAL_FILE}_{file_postfix}_PEP.csv")
    print(f"Writing to {filename}")
    with open(filename, "wb") as f:
        f.write(data)
