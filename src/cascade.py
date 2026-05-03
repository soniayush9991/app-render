def detect_cascade(system_data):
    cascade_chain = []

    db = system_data["Database API"]
    payment = system_data["Payment API"]
    auth = system_data["Auth API"]

    # Rule: DB failure propagates
    if db["latency_ms"] > 3000:
        cascade_chain.append("Database API latency spike")

        if payment["latency_ms"] > 2000:
            cascade_chain.append("Payment API impacted by DB")

        if auth["latency_ms"] > 1000:
            cascade_chain.append("Auth API degraded due to DB")

    return cascade_chain

def generate_cascade_text(chain):
    if not chain:
        return "✅ No cascading failure detected"

    result = " → ".join(chain)
    return f"🚨 Cascading Failure Path:\n{result}"