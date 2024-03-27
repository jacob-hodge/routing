import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.Graph()


locations = [(1, 1), (2, 3), (4, 2), (5, 5), (7, 4), (8, 1), (10, 3), (12, 5), (13, 2), (15, 4)]
for location in locations:
    G.add_node(location)


for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        if random.random() > 0.5:
            G.add_edge(locations[i], locations[j])


other_nodes = [(3, 1), (6, 3), (9, 2), (11, 4), (14, 3)]
for node in other_nodes:
    G.add_node(node)


for i in range(len(other_nodes)):
    for j in range(i + 1, len(other_nodes)):
        if random.random() > 0.5:
            G.add_edge(other_nodes[i], other_nodes[j])


start_location = random.choice(locations)


route = list(nx.dfs_edges(G, source=start_location))
route = [start_location] + [node for _, node in route]

print("Selected route:", route)

pos = dict((node, node) for node in G.nodes())
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue')
plt.title("Map with Roads")
plt.show()


nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightblue')
nx.draw_networkx_nodes(G, pos, nodelist=route, node_color='red', node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=[(route[i], route[i + 1]) for i in range(len(route) - 1)], edge_color='red', width=2)
plt.title("Route")
plt.show()

