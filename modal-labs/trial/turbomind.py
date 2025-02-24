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

MODEL_NAME = "radna/deepseek-r1-14b-dyve-AWQ"
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
    print(len(response))
    answers = [extract_boxed_text(res.text) for res in response]
    print(answers)
    print(select_answer(answers))

    start = time.time()
    response = pipe(
        [
            "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.\nFred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements."
            for _ in range(MAX_NUM_SEQS)
        ],
        gen_config=gen_config,
    )
    """ response = pipe(
        [
            "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.\nFred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements."
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

    return

    llm = LLM(
        llm_model_pth,
        # dtype="half",                # The data type for the model weights and activations
        max_num_seqs=MAX_NUM_SEQS,  # Maximum number of sequences per iteration. Default is 256
        max_model_len=MAX_MODEL_LEN,  # Model context length
        trust_remote_code=True,  # Trust remote code (e.g., from HuggingFace) when downloading the model and tokenizer
        enable_prefix_caching=True,
        tensor_parallel_size=1,  # The number of GPUs to use for distributed execution with tensor parallelism
        gpu_memory_utilization=0.95,  # The ratio (between 0 and 1) of GPU memory to reserve for the model
        seed=2024,
    )

    import vllm

    print(vllm.__version__)

    tokenizer = llm.get_tokenizer()
    import re

    def count_tokens(text: str) -> int:
        return len(tokenizer.encode(text))

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

    def batch_text_complete(
        completion_texts: list[str], num_reserved_tokens=0
    ) -> list[str]:

        sampling_params = [
            SamplingParams(
                temperature=0.6,  # randomness of the sampling
                min_p=0.01,
                skip_special_tokens=True,  # Whether to skip special tokens in the output
                max_tokens=MAX_MODEL_LEN
                - count_tokens(completion_text)
                - num_reserved_tokens,
                # logit_bias={x:-1 for x in [144540, 21103, 48053, 9848, 96736, 13187, 104995, 94237, 44868, 3968]},
                # logit_bias={x:-5 for x in [14190]},
                stop=["</think>"],
            )
            for completion_text in completion_texts
        ]

        request_output = llm.generate(
            prompts=completion_texts,
            sampling_params=sampling_params,
        )

        sort_keys_and_completion_texts: list[tuple[int, str]] = []

        for completion_text, single_request_output in zip(
            completion_texts, request_output
        ):
            completion_text += single_request_output.outputs[0].text
            sort_keys_and_completion_texts.append(
                (len(single_request_output.outputs[0].token_ids), completion_text)
            )

        print([sort_key for sort_key, _ in sort_keys_and_completion_texts])
        sort_keys_and_completion_texts.sort(
            key=lambda sort_key_and_completion_text: sort_key_and_completion_text[0]
        )
        print([sort_key for sort_key, _ in sort_keys_and_completion_texts])

        completion_texts = [
            completion_text for _, completion_text in sort_keys_and_completion_texts
        ]

        return completion_texts

    def create_starter_text(question: str, index: int) -> str:
        options = []
        for _ in range(1):
            options.append(
                [
                    {
                        "role": "system",
                        "content": "You are a helpful and harmless math assistant. Please reason step by step. Only work with exact numbers. Only submit an answer if you are sure. After you get your final answer, take modulo 1000, and return the final answer within \\boxed{}.",
                    },
                    {"role": "user", "content": question},
                ]
            )

        starter_text = options[index % len(options)]

        res = tokenizer.apply_chat_template(
            conversation=starter_text, tokenize=False, add_generation_prompt=True
        )

        return res

    def create_estimation_prompt(completion_text: str) -> str:
        return (
            completion_text
            + "\n\nOh, I suddenly got the answer to the whole problem, Final Answer: \\boxed{"
        )

    def predict_for_question(question: str) -> int:
        import os

        # selected_questions_only: bool = True
        selected_questions_only = False
        if selected_questions_only and not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
            # if "circumcircle" not in question:
            #    return 210
            if (
                "Triangle" not in question
                and "airline" not in question
                and "circumcircle" not in question
            ):
                return 210

        if time.time() > cutoff_time:
            return 210

        num_reserved_tokens: int = 40
        if time.time() > cutoff_times[-1]:
            num_reserved_tokens = -1 * (MAX_MODEL_LEN // 2)

        completion_texts: list[str] = [
            create_starter_text(question, index) for index in range(MAX_NUM_SEQS)
        ]
        completion_texts: list[str] = batch_text_complete(
            completion_texts, num_reserved_tokens=num_reserved_tokens
        )
        completion_answers: list[str] = [
            extract_boxed_text(completion_text) for completion_text in completion_texts
        ]
        print(completion_answers)

        answer: int = select_answer(completion_answers)
        data = {
            "question": [question] * len(completion_texts),
            "completion_text": completion_texts,
            "completion_answer": completion_answers,
        }

        if time.time() < cutoff_times[-1] and answer == -1:
            estimation_texts: list[str] = [
                create_estimation_prompt(completion_text)
                for completion_text in completion_texts
            ]
            estimation_texts: list[str] = batch_text_complete(
                estimation_texts, num_reserved_tokens=1
            )
            estimated_answers: list[str] = [
                extract_boxed_text(estimation_text)
                for estimation_text in estimation_texts
            ]
            print(estimated_answers)

            answer = select_answer(estimated_answers)
            data["estimation_text"] = estimation_texts
            data["estimated_answer"] = estimated_answers

        if not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
            df = pd.DataFrame(data)
            df.to_csv(f"{str(int(time.time() - start_time)).zfill(5)}.csv", index=False)

        print(answer, "\n\n")

        if answer == -1:
            answer = 210

        cutoff_times.pop()
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

    predict_for_question(
        "Fred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements.)"
    )
    predict_for_question(
        "We call a sequence $a_1, a_2, \\ldots$ of non-negative integers \\textit{delightful} if there exists a positive integer $N$ such that for all $n > N$, $a_n = 0$, and for all $i \\geq 1$, $a_i$ counts the number of multiples of $i$ in $a_1, a_2, \\l\\dots, a_N$. How many delightful sequences of non-negative integers are there?"
    )
    predict_for_question(
        "Let $ABC$ be a triangle with $BC=108$, $CA=126$, and $AB=39$. Point $X$ lies on segment $AC$ such that $BX$ bisects $\\angle CBA$. Let $\\omega$ be the circumcircle of triangle $ABX$. Let $Y$ be a point on $\\omega$ different from $X$ such that $CX=CY$. Line $XY$ meets $BC$ at $E$. The length of the segment $BE$ can be written as $\\frac{m}{n}$, where $m$ and $n$ are coprime positive integers. Find $m+n$."
    )
    predict_for_question(
        "Three airline companies operate flights from Dodola island. Each company has a different schedule of departures. The first company departs every 100 days, the second every 120 days and the third every 150 days. What is the greatest positive integer $d$ for which it is true that there will be $d$ consecutive days without a flight from Dodola island, regardless of the departure times of the various airlines?"
    )
    predict_for_question(
        "For positive integers $x_1,\\ldots, x_n$ define $G(x_1, \\ldots, x_n)$ to be the sum of their $\\frac{n(n-1)}{2}$ pairwise greatest common divisors. We say that an integer $n \\geq 2$ is \\emph{artificial} if there exist $n$ different positive integers $a_1, ..., a_n$ such that \
\\[a_1 + \\cdots + a_n = G(a_1, \\ldots, a_n) +1.\\] \
Find the sum of all artificial integers $m$ in the range $2 \\leq m \\leq 40$."
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
