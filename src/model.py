import joblib
import numpy as np
from pathlib import Path

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