import random

def simulate_api(api_name):
    if api_name == "Payment API":
        return {
            "latency_ms": random.randint(500, 4000),
            "cpu": random.randint(40, 90),
            "memory": random.randint(300, 1500),
            "retry": random.randint(0, 3),
            "error_rate": round(random.uniform(0.01, 0.3), 2),
            "avg_latency": random.randint(400, 1200)
        }

    elif api_name == "Auth API":
        return {
            "latency_ms": random.randint(200, 2000),
            "cpu": random.randint(20, 70),
            "memory": random.randint(200, 800),
            "retry": random.randint(0, 2),
            "error_rate": round(random.uniform(0.01, 0.2), 2),
            "avg_latency": random.randint(200, 800)
        }

    elif api_name == "Database API":
        return {
            "latency_ms": random.randint(800, 5000),
            "cpu": random.randint(50, 95),
            "memory": random.randint(500, 2000),
            "retry": random.randint(1, 4),
            "error_rate": round(random.uniform(0.05, 0.4), 2),
            "avg_latency": random.randint(600, 1500)
        }

def simulate_system():
    db = simulate_api("Database API")
    payment = simulate_api("Payment API")
    auth = simulate_api("Auth API")

    # Cascading effect
    if db["latency_ms"] > 3000:
        payment["latency_ms"] += 1000
        payment["error_rate"] += 0.2
        auth["latency_ms"] += 500
        auth["error_rate"] += 0.1

    return {
        "Database API": db,
        "Payment API": payment,
        "Auth API": auth
    }