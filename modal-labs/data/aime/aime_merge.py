# read aime_2025_I.csv, and merge with aime_2025_II.csv, both has id, problem and answer column
import pandas as pd
import numpy as np

# merge
df = pd.read_csv("aime_2025_I.csv")
df2 = pd.read_csv("aime_2025_II.csv")

df = pd.concat([df, df2])
# create unique id column for each row
import uuid 
df["id"] = df.apply(lambda x: str(uuid.uuid4()), axis=1)

df.to_csv("aime_2025.csv", index=False)
