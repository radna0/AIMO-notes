import json
import csv
import math
import random


def process_jsonl():
    # Read the JSONL file
    with open("aime2025.jsonl", "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f]

    # Process each entry
    for index, item in enumerate(data):
        # add "id" field if it doesn't exist, with random value
        if "id" not in item:
            item["id"] = index + 1

        item.pop("solution", None)
        item.pop("url", None)

        # if "question", move to "problem"
        if "question" in item:
            item["problem"] = item.pop("question")

        # Convert "answer" to an integer if it's a numeric string
        if (
            "answer" in item
            and isinstance(item["answer"], str)
            and item["answer"].isdigit()
        ):
            item["answer"] = int(item["answer"])

    # Save to CSV
    csv_columns = list(data[0].keys()) if data else []
    with open("aimo_2025_I.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    process_jsonl()
