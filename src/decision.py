def decide_action(root_cause):
    if root_cause == "DATABASE_FAILURE":
        return "Scale Database"
    elif root_cause == "AUTH_FAILURE":
        return "Refresh Token"
    elif root_cause == "TIMEOUT":
        return "Retry Request"
    elif root_cause == "Expired authentication token":
        return "Refresh authentication token immediately"
    else:
        return "No Action"
    
def calculate_severity(data):
    if data["latency_ms"] > 3000 or data["cpu"] > 80:
        return "HIGH"
    elif data["latency_ms"] > 1500:
        return "MEDIUM"
    else:
        return "LOW"
    
def generate_summary(root_cause, action, severity):
    return (
        f"Incident detected: {root_cause}\n"
        f"Severity: {severity}\n"
        f"Recommended action: {action}"
    )

def generate_alert(severity, root_cause):
    if severity == "HIGH":
        return f"🚨 CRITICAL ALERT: {root_cause} detected. Immediate action required!"
    elif severity == "MEDIUM":
        return f"⚠️ Warning: {root_cause} detected. Monitor closely."
    else:
        return "✅ System stable"

def generate_explanation(data, root_cause):
    return (
        f"The system observed elevated latency ({data['latency_ms']} ms), "
        f"CPU usage at {data['cpu']}%, and memory usage at {data['memory']} MB.\n\n"
        f"Based on these signals, the model identified {root_cause} as the most likely cause. "
        "This suggests a performance bottleneck likely due to system overload or dependency failure."
    )

def calculate_health_score(data):
    score = 100

    if data["latency_ms"] > 2000:
        score -= 30
    if data["cpu"] > 80:
        score -= 30
    if data["memory"] > 1500:
        score -= 20

    return max(score, 0)