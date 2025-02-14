import os
import modal
import subprocess


app = modal.App("limo-eval-vllm-notebook")


N_GPU = 1  # tip: for best results, first upgrade to more powerful GPUs, and only then increase GPU count

MINUTES = 60  # seconds
HOURS = 60 * MINUTES


# MODEL_NAME = "casperhansen/deepseek-r1-distill-qwen-14b-awq"

# Modified Version of AWQ
# MODEL_NAME = "radna/deepseek-r1-distill-qwen-7b-awq"

# NON-AWQ BUT Still Very Fast
MODEL_NAME = "radna/OpenR1-Qwen-7B"

# VERY SLOW
# MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"


EVAL_FILE = "aime_2025_II"


def hf_download():
    from huggingface_hub import hf_hub_download, snapshot_download

    deepseek_model = snapshot_download(
        MODEL_NAME,
        cache_dir="/cache",
    )


vol = modal.Volume.from_name("hf-hub-cache", create_if_missing=True)


vllm_image = (
    modal.Image.from_registry("ubuntu:22.04", add_python="3.12")
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

    # MAX_NUM_SEQS = 24
    # MAX_MODEL_LEN = 10 * 1024

    # BEST FOR 14B
    # MAX_NUM_SEQS = 16
    # MAX_MODEL_LEN = 8192 * 3 // 2

    # MAX_NUM_SEQS = 12
    # MAX_MODEL_LEN = 8192 * 3 // 2

    # MAX_NUM_SEQS = 32
    # MAX_MODEL_LEN = 8192 * 3 // 2

    # BEST FOR 7B
    MAX_NUM_SEQS = 32
    MAX_MODEL_LEN = 1024 * 16

    FINAL_EVAL_NAME = f"7B_NAWQ_OpenR1_{MAX_NUM_SEQS}x{MAX_MODEL_LEN}"

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
        # quantization="moe_wna16",
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
        # if time.time() > cutoff_times[-1]:
        #     print("Speedrun")
        #     # max_tokens = 2 * MAX_MODEL_LEN // 3

        sampling_params = SamplingParams(
            temperature=1.0,  # randomness of the sampling
            min_p=0.01,
            skip_special_tokens=True,  # Whether to skip special tokens in the output
            max_tokens=max_tokens,
            # stop=["</think>"],
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

    def batch_message_filter(list_of_messages) -> tuple[list[list[dict]], list[str]]:
        extracted_answers = []
        list_of_messages_to_keep = []
        for messages in list_of_messages:
            answer = extract_boxed_text(messages[-1]["content"])
            if answer:
                extracted_answers.append(answer)
            else:
                list_of_messages_to_keep.append(messages)
        return list_of_messages_to_keep, extracted_answers

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
                    "content": 'Please carefully read the problem statement first to ensure you fully understand its meaning and key points. Then, solve the problem correctly and completely through deep reasoning. Finally, return the result modulo 1000 and enclose it in \\boxed{} like "Atfer take the result modulo 1000, final anwer is \\boxed{180}.',
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
        # cutoff_times.pop()
        return answer

    # Replace this function with your inference code.
    # The function should return a single integer between 0 and 999, inclusive.
    # Each prediction (except the very first) must be returned within 30 minutes of the question being provided.

    # Path to the temporary CSV file
    TEMP_CSV = "evals_reference.csv"

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

    # drop id column = 3, 6, 7, 10, 12, 15
    pd.read_csv("reference.csv").drop("answer", axis=1).to_csv(
        "pure_reference.csv", index=False
    )

    def sample_and_predict(csv_file: str) -> None:
        """
        Reads all rows from the given CSV file, and for each row,
        calls the predict() function to process the problem.
        """
        # Attempt to read the CSV file.
        try:
            df = pd.read_csv(csv_file)
        except Exception as e:
            print("Error reading CSV:", e)
            # If the file fails to load, use a dummy DataFrame.
            df = pd.DataFrame(
                {
                    "id": [1, 2, 3],
                    "problem": [
                        "What is 2+2?",
                        "What is the capital of France?",
                        "How many days are in a year?",
                    ],
                }
            )

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
        predictions_path = "evals_reference.csv"  # or 'temporary_predictions.csv' if that's what you named it

        # Load the reference data with the correct answers.
        # (Do not drop the 'answer' column here!)
        reference_df = pd.read_csv(reference_input_path)

        # Load your temporary predictions (which should include at least 'id' and 'answer')
        predictions_df = pd.read_csv(predictions_path)

        # Merge the predictions with the reference data on the common 'id' column.
        # If both DataFrames have an 'answer' column, the merged DataFrame will have these as 'answer_x' and 'answer_y'.
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
        accuracy = correct / total if total > 0 else 0

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
        reference_df.to_csv(evals_csv_buffer, index=False)
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
