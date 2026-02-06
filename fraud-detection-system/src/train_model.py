import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, classification_report

# Load features
df = pd.read_csv("data/features.csv")

features = [
    "high_velocity",
    "location_mismatch",
    "amount_deviation",
    "high_amount"
]

X = df[features]
y = df["is_fraud"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# 🔥 FINTECH WAY: PROBABILITY-BASED PREDICTION
probs = model.predict_proba(X_test)[:, 1]

# 🔥 CUSTOM FRAUD THRESHOLD
threshold = 0.15
preds = (probs >= threshold).astype(int)

# Metrics
print("🎯 Precision:", round(precision_score(y_test, preds), 3))
print("🎯 Recall:", round(recall_score(y_test, preds), 3))
print("\nClassification Report:\n", classification_report(y_test, preds))

# Risk score example
risk_scores = (probs * 100).astype(int)
print("\nSample Risk Scores:", risk_scores[:10])

