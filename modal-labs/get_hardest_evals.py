hard_questions = [
    "2016-I-7",
    "2019-I-13",
    "2018-II-15",
    "2015-I-14",
    "1990-11",
    "1999-6",
    "1995-11",
    "2006-I-7",
    "1991-4",
    "2004-I-10",
    "2013-I-11",
    "2021-I-11",
    "2009-II-12",
    "1985-4",
    "2009-I-12",
    "2002-I-9",
    "2010-I-13",
    "2009-I-15",
    "2005-I-15",
    "2019-II-7",
    "2018-I-9",
    "2016-II-7",
    "2020-I-11",
    "2015-I-5",
    "2017-II-9",
    "2011-II-14",
    "2023-I-7",
    "2020-I-5",
    "2018-II-14",
    "2017-II-14",
    "2011-I-12",
    "2006-I-8",
    "2022-I-7",
    "2018-II-10",
    "2014-I-5",
    "2017-I-12",
    "2020-II-10",
    "2019-II-15",
    "2020-I-15",
    "2016-II-13",
    "2015-II-9",
    "2013-II-6",
    "2006-II-7",
    "1994-14",
    "2021-I-12",
    "2008-I-13",
    "2001-II-14",
    "2000-II-10",
    "2022-II-15",
    "2014-I-1",
    "2004-II-14",
    "2023-II-11",
    "2005-I-9",
    "2023-II-13",
    "2016-I-10",
    "2020-I-10",
    "2023-II-15",
    "2023-II-14",
    "1995-1",
    "2015-I-15",
    "1992-6",
    "1994-15",
    "2020-I-1",
    "2017-I-14",
    "2003-I-13",
    "2006-I-14",
    "2020-I-14",
    "1995-3",
    "2015-I-6",
    "2016-II-10",
    "2003-I-15",
    "2023-II-10",
    "2017-I-11",
    "2014-II-15",
    "2024-II-15",
    "2025-13",
    "2019-II-13",
    "2010-I-8",
    "2007-II-15",
    "2016-I-15",
    "2007-II-11",
    "2021-II-15",
    "2025-9",
    "2000-I-13",
    "2009-I-10",
    "1986-15",
    "2004-I-14",
    "2025-15",
    "2021-I-10",
    "2017-II-13",
    "2023-II-12",
    "1994-12",
    "2018-I-7",
    "2009-II-9",
    "2021-I-14",
    "2023-II-7",
    "2004-I-4",
    "2011-I-14",
    "2000-I-14",
    "2007-I-12",
    "2015-I-9",
    "2013-I-12",
    "1989-11",
    "2003-II-14",
    "2022-II-8",
    "2019-I-11",
    "1985-15",
    "2020-II-15",
    "1990-13",
    "2006-II-9",
    "2025-7",
    "1996-13",
    "2018-I-14",
    "2013-II-14",
    "2022-II-5",
    "1986-9",
    "2022-I-11",
    "2002-I-5",
    "2006-I-10",
    "2001-II-13",
    "2007-I-14",
    "2011-I-7",
    "2014-I-15",
    "2021-II-10",
    "2022-II-14",
    "1995-14",
    "2007-I-10",
    "1996-9",
    "2016-I-3",
    "2000-I-15",
    "2018-I-13",
    "2010-II-15",
    "1997-6",
    "2012-I-4",
    "2018-I-10",
    "2022-I-6",
    "2016-I-14",
    "2022-II-9",
    "2023-I-14",
    "2021-II-14",
    "2006-I-15",
    "1994-11",
    "2020-II-14",
    "1990-14",
    "2004-I-9",
    "2023-I-9",
    "2020-II-12",
    "2024-II-5",
    "2012-II-4",
    "1992-5",
    "2004-I-15",
    "1988-15",
    "2006-II-13",
    "2018-II-4",
    "2022-I-8",
    "2023-II-9",
    "2023-I-12",
    "2010-II-10",
    "1993-14",
    "2000-I-12",
    "2024-II-8",
    "2021-II-8",
    "2021-II-9",
    "2019-I-12",
    "2013-I-13",
    "2021-II-11",
    "2025-10",
    "2007-I-6",
    "2016-II-14",
    "2019-II-14",
    "2021-I-15",
    "2021-I-7",
    "2019-II-5",
    "2013-II-11",
    "2009-II-15",
    "2022-I-13",
    "2017-I-13",
    "2019-II-12",
    "2006-I-12",
    "2025-14",
    "2022-I-14",
    "2008-I-7",
    "2025-11",
    "2004-II-15",
    "2004-II-13",
    "2019-I-15",
    "2002-II-4",
    "2000-II-14",
    "2014-II-9",
    "2001-II-15",
    "1987-6",
    "2018-I-15",
    "1998-15",
    "1993-9",
    "2013-II-12",
    "2001-I-15",
]


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

    # use only the hard questions
    df_shuffled = df_shuffled[df_shuffled["id"].isin(hard_questions)]

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Split into batches and write each batch to a CSV file
    num_batches = (len(df_shuffled) + batch_size - 1) // batch_size  # Ceiling division

    for i in range(num_batches):
        start_idx = i * batch_size
        batch_df = df_shuffled.iloc[start_idx : start_idx + batch_size]
        batch_file = os.path.join(output_folder, f"hard_batch_{i+1}.csv")
        batch_df.to_csv(batch_file, index=False)
        print(f"Saved batch {i+1} with {len(batch_df)} problems to {batch_file}")


if __name__ == "__main__":
    # File paths for the input CSVs
    old_csv = "data/aime_1983_2024.csv"
    new_csv = "data/aime/aimo_2025_I.csv"

    # Folder to save batches
    output_dir = os.path.join("data", "aime")

    # Process the CSV files and split into batches of 50
    process_and_split_csv(old_csv, new_csv, output_dir, batch_size=50)
