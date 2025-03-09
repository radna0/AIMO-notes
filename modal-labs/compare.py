import pandas as pd

# File paths (adjust if needed)
reference_input_path = "data/aime/hard_batch_1.csv"
predictions_path = "evals_new.csv"

# Load the CSV files
reference_df = pd.read_csv(reference_input_path)
predictions_df = pd.read_csv(predictions_path)

# Ensure the 'id' columns are strings and strip any extra whitespace
reference_df["id"] = reference_df["id"].astype(str).str.strip()
predictions_df["id"] = predictions_df["id"].astype(str).str.strip()

# Optionally, normalize the answer columns (e.g., lowercasing and stripping whitespace)
reference_df["answer"] = reference_df["answer"].astype(str).str.strip().str.lower()
predictions_df["answer"] = predictions_df["answer"].astype(str).str.strip().str.lower()

# Merge the predictions with the reference data on the common 'id' column.
merged_df = pd.merge(
    reference_df,
    predictions_df,
    on="id",
    how="inner",
    suffixes=("_ref", "_pred"),
)

# Compare the answers
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
