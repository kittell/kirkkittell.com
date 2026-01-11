import networkx as nx
import csv
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).parent

# Load nodes
f_nodes = BASE / "pandemic_nodes.csv"
nodes = []
i = -1
with open(f_nodes, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        i += 1
        if i == 0:
            continue  # skip header
        name, color = row
        nodes.append((name, {"color": color}))

# Load edges
f_edges = BASE / "pandemic_edges.csv"
edges = []
with open(f_edges, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        source, target = row
        edges.append((source, target))

G = nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

colors = [G.nodes[n]["color"] for n in G.nodes()]

plt.figure(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_color=colors,
    edge_color="gray",
    node_size=800,
    font_size=10
)
plt.tight_layout()
plt.show()
