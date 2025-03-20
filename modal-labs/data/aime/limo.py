# read limo.jsonl, drop solution collumn
import pandas as pd

df = pd.read_json("limo.jsonl", lines=True)
df = df.drop("solution", axis=1)

# turn answer into str
df["solution"] = df["answer"].astype(str)
df = df.drop("answer", axis=1)

# save as prep jsonl file
df.to_json("test_final_limo.jsonl", orient="records", lines=True)
