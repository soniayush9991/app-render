from src.logger import log_event, load_logs
import streamlit as st
from src.model import predict_root_cause
from src.decision import decide_action, calculate_severity, generate_summary

st.set_page_config(page_title="ARP Dashboard", layout="wide")

st.title("🚀 Autonomous Reliability Platform")

# Load logs at the beginning of the script
logs = load_logs()

# Ensure logs is not None or empty before proceeding
if logs is None or logs.empty:
    st.warning("No logs available. Please check the log source.")

# Layout (columns)
col1, col2, col3 = st.columns(3)

with col1:
    latency = st.slider("Latency (ms)", 0, 5000, 1000)

with col2:
    cpu = st.slider("CPU Usage (%)", 0, 100, 50)

with col3:
    memory = st.slider("Memory (MB)", 0, 2000, 500)

if st.button("Analyze System"):

    data = {
        "latency_ms": latency,
        "cpu": cpu,
        "memory": memory,
        "retry": 2,
        "error_rate": 0.1,
        "avg_latency": 800
    }

    root_cause, confidence = predict_root_cause(data)
    action = decide_action(root_cause)