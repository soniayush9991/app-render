import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = Path(__file__).resolve().parent.parent / "model.pkl"
model = joblib.load(MODEL_PATH)

def predict_root_cause(data):
    features = np.array([[
        data["latency_ms"],
        data["cpu"],
        data["memory"],
        data["retry"],
        data["error_rate"],
        data["avg_latency"]
    ]])

    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features).max()

    return prediction, round(confidence, 2)

def retrain_model(logs_df):
    if logs_df.empty or len(logs_df) < 10:
        return False  # Not enough data

    # Prepare features and labels
    features = logs_df[["latency", "cpu", "memory"]].values
    labels = logs_df["root_cause"].values

    # Simple retraining: fit a new model or update existing
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save updated model
    joblib.dump(model, MODEL_PATH)
    return True