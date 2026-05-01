def decide_action(root_cause):
    if root_cause == "DATABASE_FAILURE":
        return "Scale Database"
    elif root_cause == "AUTH_FAILURE":
        return "Refresh Token"
    elif root_cause == "TIMEOUT":
        return "Retry Request"
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
    return f"""
    Incident detected: {root_cause}
    Severity: {severity}
    Recommended action: {action}
    """