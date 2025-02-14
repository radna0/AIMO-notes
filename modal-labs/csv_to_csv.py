import pandas as pd


def process_aime_dataset(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Select required columns and rename them
    df = df[["ID", "Question", "Answer"]]
    df.rename(
        columns={"ID": "id", "Question": "problem", "Answer": "answer"}, inplace=True
    )

    # Save to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Processed file saved as {output_file}")


# Example usage
process_aime_dataset("data/AIME_Dataset_1983_2024.csv", "data/aime_1983_2024.csv")
