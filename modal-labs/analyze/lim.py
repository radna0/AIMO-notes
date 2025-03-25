import json
import numpy as np
from pathlib import Path
import argparse
from datasets import load_dataset


def filter_dataset(dataset):
    """Filter dataset for numerical answers and difficulty range."""

    def convert_to_int(example):
        try:
            example["answer"] = int(example["answer"])
        except ValueError:
            example["answer"] = None
        return example

    dataset = dataset.map(convert_to_int)
    dataset = dataset.filter(lambda example: example["answer"] is not None)
    dataset = dataset.filter(lambda example: 0 <= example["answer"] <= 1000)
    dataset = dataset.filter(lambda example: 3 <= example["difficulty"] <= 8)

    return dataset


def compute_prompt_accuracies(train_samples_path):
    """Compute accuracy of each prompt based on reward values."""
    prompt_stats = {}

    for step_file in sorted(train_samples_path.glob("step_*.json")):
        with open(step_file) as f:
            step_data = json.load(f)

        for sample in step_data:
            prompt = sample["prompt"].strip()
            reward = sample.get("reward", 0)

            if prompt not in prompt_stats:
                prompt_stats[prompt] = [0, 0]  # [correct_count, total_count]

            prompt_stats[prompt][1] += 1
            if reward == 1:
                prompt_stats[prompt][0] += 1

    # Compute accuracy per prompt
    return {
        prompt: correct / total
        for prompt, (correct, total) in prompt_stats.items()
        if total > 0
    }


def select_best_prompts(prompt_accuracies, threshold=0.8):
    """Select prompts with consistently high accuracy."""
    return {prompt for prompt, acc in prompt_accuracies.items() if acc >= threshold}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Filter high-quality prompts for training"
    )
    parser.add_argument(
        "--train_samples_path",
        type=str,
        required=True,
        help="Path to the training samples directory",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="high_value_data.json",
        help="Output file for filtered data",
    )
    parser.add_argument(
        "--accuracy_threshold",
        type=float,
        default=0.8,
        help="Minimum accuracy threshold for selecting prompts",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    train_samples_path = Path(args.train_samples_path)

    # Load HuggingFace dataset
    dataset = load_dataset("KbsdJames/Omni-MATH", split="test")
    dataset = filter_dataset(dataset)

    # Compute prompt accuracies
    prompt_accuracies = compute_prompt_accuracies(train_samples_path)

    # Select best prompts
    selected_prompts = select_best_prompts(prompt_accuracies, args.accuracy_threshold)

    # Filter original dataset
    with open(args.original_prompts_path) as f:
        original_data = json.load(f)

    high_value_data = [
        sample for sample in original_data if sample["prompt"] in selected_prompts
    ]

    # Save filtered data
    with open(args.output_path, "w") as f:
        json.dump(high_value_data, f)

    print(f"Selected {len(high_value_data)} high-value prompts.")


if __name__ == "__main__":
    main()
