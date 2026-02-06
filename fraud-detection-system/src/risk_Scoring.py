import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load data
df = pd.read_csv("data/features.csv")

features = [
    "high_velocity",
    "location_mismatch",
    "amount_deviation",
    "high_amount"
]

X = df[features]
y = df["is_fraud"]

# Train model on full data
model = RandomForestClassifier(
    n_estimators=300,
    class_weight="balanced",
    random_state=42
)
model.fit(X, y)

# Probability-based risk
df["fraud_probability"] = model.predict_proba(X)[:, 1]
df["risk_score"] = (df["fraud_probability"] * 100).astype(int)

# Risk buckets
def bucket(score):
    if score >= 70:
        return "HIGH"
    elif score >= 30:
        return "MEDIUM"
    return "LOW"

df["risk_bucket"] = df["risk_score"].apply(bucket)

# 🔥 TOP 1% RISKY TRANSACTIONS
top_risky = df.sort_values("risk_score", ascending=False).head(int(0.01 * len(df)))

# Save outputs
df.to_csv("data/final_risk_scores.csv", index=False)
top_risky.to_csv("data/top_1_percent_risky_transactions.csv", index=False)

print("✅ Risk scoring completed")
print("🔥 Top 1% risky transactions exported")
