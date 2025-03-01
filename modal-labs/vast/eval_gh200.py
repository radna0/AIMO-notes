HF_TOKEN = "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"


def hf_download(model_name):
    from huggingface_hub import hf_hub_download, snapshot_download

    deepseek_model = snapshot_download(
        model_name,
        cache_dir="cache/",
        token=HF_TOKEN,
    )


def main(args):
    MODEL_NAME = args.model
    hf_download(MODEL_NAME)

    EVAL_FILE = args.file
    print(f"Using evaluation file: {EVAL_FILE}")

    # copy file from ../data/aime/{EVAL_FILE}.csv to reference.csv
    import shutil
    import os

    os.makedirs("tmp", exist_ok=True)
    os.makedirs("evals_res", exist_ok=True)
    shutil.copy(f"evals/{EVAL_FILE}", "tmp/reference.csv")

    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    # os.environ["VLLM_USE_V1"] = "1"

    # On GH200, Set to "spawn", default is "fork"
    # os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn"

    os.environ["VLLM_FLASH_ATTN_VERSION"] = "3"  # on h100 and above

    import time
    import warnings

    import pandas as pd
    import polars as pl
    import numpy as np

    import torch

    pd.set_option("display.max_colwidth", None)
    start_time = time.time()
    # cutoff_time = start_time + (1 * 60 + 40) * 60
    """ cutoff_times = [
        int(x) for x in np.linspace(cutoff_time, start_time + 10 * 60, 80 + 1)
    ] """

    from vllm import LLM, SamplingParams

    warnings.simplefilter("ignore")

    llm_model_pth = MODEL_NAME

    MAX_NUM_SEQS = args.num_seqs
    MAX_MODEL_LEN = 1024 * 12
    EVAL = True
    EVAL_SELECTED_QUESTIONS_ONLY = False

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
        completion_texts: list[str], num_reserved_tokens=0, cur_max_model_len=0
    ) -> list[str]:

        print(f"Using cur_max_model_len: {cur_max_model_len}")
        sampling_params = [
            SamplingParams(
                temperature=0.6,  # randomness of the sampling
                min_p=0.01,
                skip_special_tokens=True,  # Whether to skip special tokens in the output
                max_tokens=cur_max_model_len
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

    def create_starter_messages(question: str, index: int) -> str:
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
        import time

        start_time = time.time()

        if not EVAL and not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
            return 210

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

        """ if time.time() > cutoff_time:
            return 210 """

        print(question)
        num_reserved_tokens: int = 40

        cur_max_model_len = args.tokens
        """ if time.time() > cutoff_times[-1]:
            cur_max_model_len = MAX_MODEL_LEN """

        completion_texts: list[str] = [
            create_starter_messages(question, index) for index in range(MAX_NUM_SEQS)
        ]
        completion_texts: list[str] = batch_text_complete(
            completion_texts,
            num_reserved_tokens=num_reserved_tokens,
            cur_max_model_len=cur_max_model_len,
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

        """ guess_time = time.time()
        guess = 3
        idx = 0
        while idx < guess and answer == -1:
            estimation_texts: list[str] = [
                create_estimation_prompt(completion_text)
                for completion_text in completion_texts
            ]
            estimation_texts: list[str] = batch_text_complete(
                estimation_texts,
                num_reserved_tokens=1,
                cur_max_model_len=cur_max_model_len,
            )
            estimated_answers: list[str] = [
                extract_boxed_text(estimation_text)
                for estimation_text in estimation_texts
            ]
            print(estimated_answers)

            answer = select_answer(estimated_answers)
            data["estimation_text"] = estimation_texts
            data["estimated_answer"] = estimated_answers
            idx += 1

        print(f"Guess Time taken: {time.time() - guess_time}") """

        if not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
            df = pd.DataFrame(data)
            df.to_csv(
                f"tmp/{str(int(time.time() - start_time)).zfill(5)}.csv", index=False
            )

        print(answer, "\n\n")

        if answer == -1:
            answer = 210
        print(f"Time taken: {time.time() - start_time}")
        # cutoff_times.pop()
        return answer

    # Replace this function with your inference code.
    # The function should return a single integer between 0 and 999, inclusive.
    # Each prediction (except the very first) must be returned within 30 minutes of the question being provided.

    # Path to the temporary CSV file
    import uuid

    uid = str(uuid.uuid4())

    TEMP_CSV = f"tmp/evals_{uid}_{EVAL_FILE}.csv"

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
        "Fred and George take part in a tennis tournament with $4046$ other players. In each round, the players are paired into $2024$ matches. How many ways are there to arrange the first round such that Fred and George do not have to play each other? (Two arrangements for the first round are \\textit{different} if there is a player with a different opponent in the two arrangements.)"
    )
    predict_for_question(
        "Triangle $ABC$ has side length $AB = 120$ and circumradius $R = 100$. Let $D$ be the foot of the perpendicular from $C$ to the line $AB$. What is the greatest possible length of segment $CD$?"
    )

    return """

    pd.read_csv("tmp/reference.csv").drop("answer", axis=1).to_csv(
        "tmp/pure_reference.csv", index=False
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

    sample_and_predict("tmp/pure_reference.csv")

    # if EVAL and not EVAL_SELECTED_QUESTIONS_ONLY and not os.getenv('KAGGLE_IS_COMPETITION_RERUN'):
    if (
        EVAL
        and not EVAL_SELECTED_QUESTIONS_ONLY
        and not os.getenv("KAGGLE_IS_COMPETITION_RERUN")
    ):
        import pandas as pd

        # File paths (adjust if needed)
        reference_input_path = "tmp/reference.csv"
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

        # save the merged DataFrame to a new CSV file
        # randomize with uuid
        merged_df.to_csv(f"evals_res/evals_{uid}_{EVAL_FILE}.csv", index=False)


if __name__ == "__main__":
    import argparse
    import time

    start = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        default="casperhansen/deepseek-r1-distill-qwen-7b-awq",
        help="Model to use",
    )
    parser.add_argument(
        "--file",
        type=str,
        default="hard_batch_1",
        help="Eval File to use",
    )
    parser.add_argument(
        "--num_seqs",
        type=int,
        default=48,
        help="Number of sequences to generate per prompt",
    )
    parser.add_argument(
        "--tokens",
        type=int,
        default=1024 * 12,
        help="Number of sequences to generate per prompt",
    )

    args = parser.parse_args()
    main(args)

    print(f"Time Taken: {time.time() - start}")
