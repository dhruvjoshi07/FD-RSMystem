import pandas as pd

df = pd.read_csv("data/clean_transactions.csv", parse_dates=["txn_time"])
df = df.sort_values(["user_id", "txn_time"])

# 1️⃣ Transaction velocity (within 5 minutes)
df["prev_time"] = df.groupby("user_id")["txn_time"].shift(1)
df["time_diff_sec"] = (df["txn_time"] - df["prev_time"]).dt.total_seconds()
df["high_velocity"] = (df["time_diff_sec"] < 300).fillna(0).astype(int)

# 2️⃣ Location mismatch
df["location_mismatch"] = (df["country"] != df["ip_country"]).astype(int)

# 3️⃣ Amount deviation from user average
user_avg = df.groupby("user_id")["amount"].transform("mean")
df["amount_deviation"] = (df["amount"] / user_avg).fillna(1)

# 4️⃣ High amount flag (top 5%)
df["high_amount"] = (df["amount"] > df["amount"].quantile(0.95)).astype(int)

df.to_csv("data/features.csv", index=False)
print("✅ Features engineered → data/features.csv created")
