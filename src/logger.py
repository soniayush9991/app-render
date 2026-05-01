import pandas as pd
import os

LOG_FILE = "logs.csv"

def log_event(data, root_cause, action, severity, confidence):
    record = {
        "latency": data["latency_ms"],
        "cpu": data["cpu"],
        "memory": data["memory"],
        "root_cause": root_cause,
        "action": action,
        "severity": severity,
        "confidence": confidence
    }

    df = pd.DataFrame([record])

    if os.path.exists(LOG_FILE):
        df.to_csv(LOG_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(LOG_FILE, index=False)

def load_logs():
    if os.path.exists(LOG_FILE):
        return pd.read_csv(LOG_FILE)
    return pd.DataFrame()