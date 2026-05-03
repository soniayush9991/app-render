import csv
import os
import pandas as pd

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

    write_header = not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0
    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(record.keys()))
        if write_header:
            writer.writeheader()
        writer.writerow(record)


def load_logs():
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame()

    try:
        return pd.read_csv(LOG_FILE)
    except pd.errors.ParserError:
        valid_rows = []
        with open(LOG_FILE, newline="") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            if header is None:
                return pd.DataFrame()

            expected_columns = len(header)
            for row in reader:
                if len(row) == expected_columns:
                    valid_rows.append(row)

        cleaned = pd.DataFrame(valid_rows, columns=header)
        cleaned.to_csv(LOG_FILE, index=False)
        return cleaned