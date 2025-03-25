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
    import time

    start_time = time.time()

    os.makedirs("tmp", exist_ok=True)
    os.makedirs("evals_res", exist_ok=True)

    # get base path for eval_file
    EVAL_FILE_BASENAME = os.path.basename(EVAL_FILE)
    MODEL_NAME_STR = "+".join(args.model.split("/"))
    SAVED_EVAL_FILE = f"{str(start_time)}_{MODEL_NAME_STR}_{EVAL_FILE_BASENAME}_seq{args.num_seqs}_tok{args.tokens}_q{args.quant_policy}_tpp{args.top_p}_mnp{args.min_p}_tpk{args.top_k}"

    import os

    os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    os.environ["TRITON_PTXAS_PATH"] = "/usr/local/cuda/bin/ptxas"
    import re
    import random
    import warnings
    from collections import Counter
    import numpy as np, pandas as pd, polars as pl

    import torch
    import lmdeploy
    from lmdeploy import pipeline, TurbomindEngineConfig, GenerationConfig
    from transformers import AutoTokenizer

    warnings.simplefilter("ignore")
    print("PyTorch version:", torch.__version__)
    print("LMDeploy:", lmdeploy.__version__)

    def seed_everything(seed):
        os.environ["PYTHONHASHSEED"] = str(seed)
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.benchmark = True
        torch.backends.cudnn.deterministic = True

    seed_everything(seed=0)

    # cutoff_time = start_time + (1 * 60 + 50) * 60
    # cutoff_times = [
    #     int(x) for x in np.linspace(cutoff_time, start_time + 10 * 60, 50 + 1)
    # ]

    llm_model_pth = MODEL_NAME

    MAX_NUM_SEQS = args.num_seqs
    MAX_MODEL_LEN = 1024 * 12
    EVAL = True
    EVAL_SELECTED_QUESTIONS_ONLY = False

    engine_config = TurbomindEngineConfig(
        # tp=1,
        quant_policy=args.quant_policy,
        cache_max_entry_count=0.95,
        session_len=MAX_MODEL_LEN,
        enable_prefix_caching=True,
        max_batch_size=MAX_NUM_SEQS,
    )

    pipe = pipeline(llm_model_pth, backend_config=engine_config)

    tokenizer = AutoTokenizer.from_pretrained(llm_model_pth, trust_remote_code=False)

    import re

    def extract_boxed_text(text):
        pattern = r"oxed{(.*?)}"
        matches = re.findall(pattern, text)
        if not matches:
            return ""
        for match in matches[::-1]:
            if match != "":
                return match
        return ""

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
        max_tokens = args.tokens
        # if time.time() > cutoff_times[-1]:
        #     print("Speedrun")
        #     max_tokens = 1024 * 8

        list_of_texts = [
            tokenizer.apply_chat_template(
                conversation=messages, tokenize=False, add_generation_prompt=True
            )
            for messages in list_of_messages
        ]

        gen_configs = [
            GenerationConfig(
                do_sample=True,
                temperature=1.0,  # Randomness of the sampling
                top_k=args.top_k,
                top_p=args.top_p,  # Cumulative probability of the top tokens to consider
                min_p=args.min_p,  # Minimum probability for a token to be considered
                skip_special_tokens=True,  # Whether to skip special tokens in the output
                max_new_tokens=max_tokens,  # Maximum number of tokens to generate
                stop_words=["</think>"],  # List of strings that stop the generation
            )
            for prompt in list_of_texts
        ]

        request_output = pipe(
            list_of_texts,
            gen_config=gen_configs,
        )
        print(
            [
                single_request_output.generate_token_len
                for single_request_output in request_output
            ]
        )

        sort_keys_and_list_of_messages = []
        for messages, single_request_output in zip(list_of_messages, request_output):
            # print()
            # print(single_request_output.outputs[0].text)
            # print()
            messages.append(
                {"role": "assistant", "content": single_request_output.text}
            )

            sort_keys_and_list_of_messages.append(
                (single_request_output.generate_token_len, messages)
            )
        print([sort_key for sort_key, _ in sort_keys_and_list_of_messages])
        sort_keys_and_list_of_messages.sort(
            key=lambda sort_key_and_messages: sort_key_and_messages[0]
        )
        print([sort_key for sort_key, _ in sort_keys_and_list_of_messages])

        list_of_messages = [messages for _, messages in sort_keys_and_list_of_messages]
        return list_of_messages

    def create_starter_messages(question: str, index: int) -> str:
        options = []
        for _ in range(1):
            options.append(
                [
                    {
                        "role": "system",
                        "content": "You are a helpful and harmless assistant. You are Qwen developed by Alibaba. You should think step-by-step. Return final answer within \\boxed{}, after taking modulo 1000.",
                    },
                    {"role": "user", "content": question},
                ]
            )

        return options[index % len(options)]

    def predict_for_question(question: str, question_id=time.time()) -> int:
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

        """ if time.time() > cutoff_time:
            return 210 """

        print(question)

        num_seqs = MAX_NUM_SEQS

        list_of_messages = [
            create_starter_messages(question, index) for index in range(num_seqs)
        ]

        all_extracted_answers = []
        for _ in range(1):
            list_of_messages = batch_message_generate(list_of_messages)

            if not os.getenv("KAGGLE_IS_COMPETITION_RERUN"):
                df = pd.DataFrame(
                    {
                        "question": [question] * len(list_of_messages),
                        "message": [
                            messages[-1]["content"] for messages in list_of_messages
                        ],
                    }
                )
                df.to_csv(f"tmp/{str(question_id)}_{SAVED_EVAL_FILE}.csv", index=False)

            list_of_messages, extracted_answers = batch_message_filter(list_of_messages)
            all_extracted_answers.extend(extracted_answers)

        print(all_extracted_answers)
        answer = select_answer(all_extracted_answers)
        print(answer)

        print("\n\n")
        # cutoff_times.pop()
        print(f"Time taken: {time.time() - start_time}")
        return answer

    # Replace this function with your inference code.
    # The function should return a single integer between 0 and 999, inclusive.
    # Each prediction (except the very first) must be returned within 30 minutes of the question being provided.

    # Path to the temporary CSV file
    import uuid

    TEMP_CSV = f"tmp/evals_{SAVED_EVAL_FILE}.csv"

    def predict(
        id_: pl.DataFrame, question: pl.DataFrame
    ) -> pl.DataFrame | pd.DataFrame:
        id_ = id_["id"][0]
        print("------")
        print(id_)

        question = question["problem"][0]
        answer = predict_for_question(question, question_id=id_)
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

    sample_and_predict(EVAL_FILE)

    # if EVAL and not EVAL_SELECTED_QUESTIONS_ONLY and not os.getenv('KAGGLE_IS_COMPETITION_RERUN'):
    if (
        EVAL
        and not EVAL_SELECTED_QUESTIONS_ONLY
        and not os.getenv("KAGGLE_IS_COMPETITION_RERUN")
    ):
        import pandas as pd

        # File paths (adjust if needed)
        reference_input_path = EVAL_FILE
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

        std_outputs = ""
        std_outputs = std_outputs + f"Total predictions compared: {total}" + "\n"
        std_outputs = std_outputs + f"Number of correct predictions: {correct}" + "\n"
        std_outputs = std_outputs + f"Accuracy: {accuracy:.2%}" + "\n"

        # Optionally, list the rows where the prediction did not match the reference.
        incorrect_df = merged_df[~merged_df["is_correct"]]
        if not incorrect_df.empty:
            std_outputs = std_outputs + "\nIncorrect predictions:" + "\n"
            # Adjust the columns below if your CSVs have different column names.
            std_outputs = (
                std_outputs
                + str(incorrect_df[["id", "problem", "answer_ref", "answer_pred"]])
                + "\n"
            )
        else:
            std_outputs = std_outputs + "\nAll predictions match the reference!" + "\n"

        print(std_outputs)

        # write stdoutputs to evals_res/outputs_{SAVED_EVAL_FILE}.log

        # write stdoutputs to evals_res/outputs_{SAVED_EVAL_FILE}.log
        with open(f"evals_res/outputs_{SAVED_EVAL_FILE}.log", "w") as f:
            f.write(std_outputs)

        # save the merged DataFrame to a new CSV file
        # randomize with uuid
        merged_df.to_csv(f"evals_res/evals_{SAVED_EVAL_FILE}.csv", index=False)


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

    parser.add_argument(
        "--quant_policy",
        type=int,
        default=8,
        choices=[8, 4, 0],
        help="Number of sequences to generate per prompt",
    )

    parser.add_argument(
        "--top_k",
        type=int,
        default=50,
        help="Number of sequences to generate per prompt",
    )

    parser.add_argument(
        "--top_p",
        type=float,
        default=0.90,
        help="Number of sequences to generate per prompt",
    )

    parser.add_argument(
        "--min_p",
        type=float,
        default=0.05,
        help="Number of sequences to generate per prompt",
    )

    args = parser.parse_args()
    main(args)

    print(f"Time Taken: {time.time() - start}")
