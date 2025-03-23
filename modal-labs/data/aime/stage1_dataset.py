from datasets import load_dataset

# Load the dataset
dataset = load_dataset("SynthLabsAI/Big-Math-RL-Verified", split="train")


# Define a function to filter out unwanted problems
def filter_fn(example):
    try:
        # Check if the answer is a numerical value
        answer = int(example["answer"])
        if not (answer >= 0 and answer <= 1000):
            return False
    except ValueError:
        return False  # Filter out non-numerical answers

    # Filter out problems where 0.5 <= llama8b_solve_rate < 1.0
    if not example["llama8b_solve_rate"]:
        return False

    if example["llama8b_solve_rate"] < 0.5 or example["llama8b_solve_rate"] >= 0.75:
        return False

    return True


# Apply the filter
filtered_dataset = dataset.filter(filter_fn)

# Show an example of the filtered dataset
print(len(filtered_dataset))
