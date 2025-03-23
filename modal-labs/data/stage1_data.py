import csv
import json


def load_hard_batches():
    """Load all problems from hard_batch_1 to hard_batch_4.csv."""
    excluded_problems = set()
    for i in range(1, 5):  # Iterate from 1 to 4
        filename = f"aime/hard_batch_{i}.csv"
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                excluded_problems.add(row["id"])  # Collect ids to exclude
    return excluded_problems


def filter_aime_data(excluded_problems):
    """Load AIME problems, exclude hard batch problems, and save to JSONL."""
    filtered_data = []
    with open("aime_1983_2025.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                int(row["answer"])
            except ValueError:
                continue  # Skip rows with non-integer answers

            if row["id"] not in excluded_problems:  # Keep only non-excluded problems
                filtered_data.append(
                    {"question": row["problem"], "solution": row["answer"]}
                )

    # Save to stage1_aime.jsonl
    with open("stage1_aime.jsonl", "w") as f:
        print(f"Saved {len(filtered_data)} problems to stage1_aime.jsonl")
        for entry in filtered_data:
            f.write(json.dumps(entry) + "\n")


def main():
    excluded_problems = load_hard_batches()
    filter_aime_data(excluded_problems)
    print(
        f"Filtered data saved to stage1_aime.jsonl. Excluded {len(excluded_problems)} problems."
    )


if __name__ == "__main__":
    main()
