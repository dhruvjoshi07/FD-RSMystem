import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n = 5000

base_time = datetime(2024, 2, 1)

df = pd.DataFrame({
    "txn_id": [f"T{i}" for i in range(n)],
    "user_id": np.random.randint(1, 500, n),
    "amount": np.random.exponential(scale=500, size=n),
    "country": np.random.choice(["India","USA","Germany"], n),
    "ip_country": np.random.choice(["India","USA","Germany","Nigeria","Russia"], n),
    "txn_time": [
        base_time + timedelta(seconds=int(np.random.exponential(scale=300)))
        for _ in range(n)
    ],
    "is_fraud": np.random.choice([0,1], n, p=[0.95,0.05])
})

df.to_csv("data/raw/transactions.csv", index=False)
print("✅ Synthetic dataset with txn_time generated")
