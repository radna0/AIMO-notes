import csv


def main():
    all_data = []

    # Read aime_1983_2024.csv
    with open("aime_1983_2024.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        all_data.extend(reader)  # Append existing data

    # Read and modify aime_2025_I.csv
    with open("aime/aime_2025_I.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        data_2025_I = []
        for row in reader:
            row["id"] = f"2025-I-{row['id']}"
            data_2025_I.append(row)

    # Read and modify aime_2025_II.csv
    with open("aime/aime_2025_II.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        data_2025_II = []
        for row in reader:
            row["id"] = f"2025-II-{row['id']}"
            data_2025_II.append(row)

    all_data.extend(data_2025_I + data_2025_II)

    # Write to aime_1983_2025.csv
    fieldnames = ["id", "problem", "answer"]  # Ensure correct column names
    with open("aime_1983_2025.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)


if __name__ == "__main__":
    main()
