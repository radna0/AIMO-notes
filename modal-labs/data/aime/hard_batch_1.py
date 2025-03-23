# read hard_batch_234.csv, drop id collumn, and rename problem collumn to question
import pandas as pd

df = pd.read_csv("hard_batch_1.csv")
df = df.drop("id", axis=1)
df = df.rename(columns={"problem": "question"})


df["answer"] = df["answer"].astype(str)
# rename "answer" to "solution", drop "answer" collumn
df = df.rename(columns={"answer": "solution"})
# save as jsonl file
df.to_json("hard_batch_1.jsonl", orient="records", lines=True)
