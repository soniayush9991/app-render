from src.logger import log_event, load_logs
import streamlit as st
from src.model import predict_root_cause
from src.simulator import simulate_system
from src.cascade import detect_cascade, generate_cascade_text
from src.graph import build_graph, draw_graph
from src.decision import (
    decide_action,
    calculate_severity,
    generate_summary,
    generate_alert,
    generate_explanation,
    calculate_health_score
)

st.set_page_config(page_title="ARP Dashboard", layout="wide")

st.title("🚀 Autonomous Reliability Platform")

# Load logs at the beginning of the script
logs = load_logs()

if logs is None or logs.empty:
    st.warning("No logs available. Future predictions will be saved once analysis runs.")
else:
    st.sidebar.subheader("Recent logs")
    st.sidebar.dataframe(logs.tail(10))

api_choice = st.selectbox(
    "Select API Service",
    ["Payment API", "Auth API", "Database API"]
)

# Layout (columns)
col1, col2, col3 = st.columns(3)

with col1:
    latency = st.slider("Latency (ms)", 0, 5000, 1000)

with col2:
    cpu = st.slider("CPU Usage (%)", 0, 100, 50)

with col3:
    memory = st.slider("Memory (MB)", 0, 2000, 500)

if st.button("Analyze System"):
    try:
        system_data = simulate_system()
        api_data = system_data[api_choice]

        api_data["latency_ms"] = latency
        api_data["cpu"] = cpu
        api_data["memory"] = memory
        system_data[api_choice] = api_data

        graph = build_graph(system_data)
        fig = draw_graph(graph, system_data)
        cascade_chain = detect_cascade(system_data)
        cascade_text = generate_cascade_text(cascade_chain)

        # Core logic
        root_cause, confidence = predict_root_cause(api_data)
        action = decide_action(root_cause)
        severity = calculate_severity(api_data)
        summary = generate_summary(root_cause, action, severity)

        # New features
        alert = generate_alert(severity, root_cause)
        explanation = generate_explanation(api_data, root_cause)
        health_score = calculate_health_score(api_data)

        log_event(api_data, root_cause, action, severity, confidence)

        # ===== UI OUTPUT =====
        st.subheader("📡 Simulated API Signals")
        st.json(api_data)

        st.subheader("📊 Analysis Results")

        col1, col2, col3 = st.columns(3)
        col1.metric("Root Cause", root_cause)
        col2.metric("Confidence", f"{confidence * 100:.2f}%")
        col3.metric("Severity", severity)

        st.metric("API Selected", api_choice)
        st.write(summary)

        st.subheader("📡 System State")
        for api, signals in system_data.items():
            st.write(f"### {api}")
            st.json(signals)

        st.subheader("🔗 Cascading Failure Analysis")
        st.warning(cascade_text)

        st.subheader("🕸 System Dependency Graph")
        st.pyplot(fig)

        st.subheader("🛠 Recommended Action")
        st.success(action)

        st.subheader("🚨 Alert System")
        st.error(alert)

        st.subheader("🧠 AI Explanation")
        st.write(explanation)

        st.subheader("💚 System Health Score")
        st.metric("Health Score", f"{health_score}/100")

    except Exception as e:
        st.error(f"🚨 Error: {e}")