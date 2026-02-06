import pandas as pd
import os

print("📂 Current working directory:")
print(os.getcwd())

print("📁 Files in data/raw:")
print(os.listdir("data/raw"))

df = pd.read_csv("data/raw/transactions.csv")
df['txn_time'] = pd.to_datetime(df['txn_time'])

df.to_csv("data/clean_transactions.csv", index=False)
print("✅ clean_transactions.csv CREATED")
