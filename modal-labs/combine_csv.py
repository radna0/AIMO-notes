import pandas as pd
import os


def process_and_split_csv(
    old_file, new_file, output_folder, batch_size=50, random_seed=42
):
    # Read the older dataset
    df_old = pd.read_csv(old_file)

    # Read the new dataset and update the id column
    df_new = pd.read_csv(new_file)
    # Ensure id is a string and prepend "2025-"
    df_new["id"] = "2025-" + df_new["id"].astype(str)

    # Combine the datasets
    df_combined = pd.concat([df_old, df_new], ignore_index=True)

    # Shuffle the combined dataframe
    df_shuffled = df_combined.sample(frac=1, random_state=random_seed).reset_index(
        drop=True
    )

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Split into batches and write each batch to a CSV file
    num_batches = (len(df_shuffled) + batch_size - 1) // batch_size  # Ceiling division

    for i in range(num_batches):
        start_idx = i * batch_size
        batch_df = df_shuffled.iloc[start_idx : start_idx + batch_size]
        batch_file = os.path.join(output_folder, f"batch_{i+1}.csv")
        batch_df.to_csv(batch_file, index=False)
        print(f"Saved batch {i+1} with {len(batch_df)} problems to {batch_file}")


if __name__ == "__main__":
    # File paths for the input CSVs
    old_csv = "data/aime_1983_2024.csv"
    new_csv = "data/aimo_2025_I.csv"

    # Folder to save batches
    output_dir = os.path.join("data", "aime")

    # Process the CSV files and split into batches of 50
    process_and_split_csv(old_csv, new_csv, output_dir, batch_size=50)
