
import osmnx as ox
import matplotlib.pyplot as plt

# Define the area of interest in Shenzhen
place_name = "Luohu District, Shenzhen, China"

print(f"Downloading road network for: {place_name}...")
 Download the road network (driveable roads)
graph = ox.graph_from_place(place_name, network_type='drive')

# Basic stats for the professor to see
nodes = len(graph.nodes())
edges = len(graph.edges())
print(f"Graph loaded with {nodes} nodes and {edges} edges.")

# Visualize the network
fig, ax = ox.plot_graph(graph, node_size=0, edge_color='red', edge_linewidth=0.5)
plt.show()
