# Filter the HuggingFace dataset KbsdJames/Omni-MATH
# column: domain, difficulty, problem, solution, answer, source
# filter difficulty >= 3 and <= 8
from datasets import load_dataset

dataset = load_dataset("KbsdJames/Omni-MATH", split="test")


# filter problems with numerical answers, try converting to int, >= 0 and <= 1000
def convert_to_int(example):
    try:
        example["answer"] = int(example["answer"])
    except ValueError:
        example["answer"] = None
    return example


dataset = dataset.map(convert_to_int)
print(f"Dataset size after converting to int check: {len(dataset)}")
dataset = dataset.filter(lambda example: example["answer"] is not None)
print(f"Dataset size after keeping problems with numerical answers: {len(dataset)}")
dataset = dataset.filter(
    lambda example: example["answer"] >= 0 and example["answer"] <= 1000
)
print(
    f"Dataset size after removing problems with numerical answers outside [0, 1000]: {len(dataset)}"
)


# filter difficulty >= 3 and <= 8
dataset = dataset.filter(lambda example: 5 <= example["difficulty"] <= 8)

print(f"Dataset size after filtering difficulty: {len(dataset)}")
