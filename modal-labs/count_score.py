import pandas as pd

# File paths (adjust if needed)
predictions_path = "evals_new.csv"

# Load the CSV files
predictions_df = pd.read_csv(predictions_path)


# Calculate metrics
total = len(predictions_df)
correct = predictions_df["is_correct"].sum()
accuracy = correct / total

print(f"Total predictions compared: {total}")
print(f"Number of correct predictions: {correct}")
print(f"Accuracy: {accuracy:.2%}")

# Optionally, list the rows where the prediction did not match the reference.
incorrect_df = predictions_df[~predictions_df["is_correct"]]
if not incorrect_df.empty:
    print("\nIncorrect predictions:")
    # Adjust the columns below if your CSVs have different column names.
    print(incorrect_df[["id", "problem", "answer_ref", "answer_pred"]])
else:
    print("\nAll predictions match the reference!")
