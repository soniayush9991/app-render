import networkx as nx
import matplotlib.pyplot as plt

def build_graph(system_data):
    G = nx.DiGraph()

    # Nodes
    for api in system_data.keys():
        G.add_node(api, latency=system_data[api]["latency_ms"])

    # Dependencies (fixed for now)
    G.add_edge("Database API", "Payment API")
    G.add_edge("Database API", "Auth API")

    return G


def draw_graph(G, system_data):
    pos = nx.spring_layout(G)

    colors = []

    for node in G.nodes():
        latency = system_data[node]["latency_ms"]

        if latency > 3000:
            colors.append("red")
        elif latency > 1500:
            colors.append("orange")
        else:
            colors.append("green")

    plt.figure(figsize=(6, 4))
    labels = {
    node: f"{node}\nLatency: {system_data[node]['latency_ms']} ms\nCPU: {system_data[node]['cpu']}%"
    for node in G.nodes()
}
    nx.draw(
        G,
        pos,
        labels=labels,   # 👈 THIS is the key change
        with_labels=True,
        node_color=colors,
        node_size=2000,
        font_size=10,
        font_weight="bold",
        arrows=True
)

    return plt