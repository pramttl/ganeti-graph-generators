# Using networkx and matplotlib to visualize Ganeti Cluster Configuration.
# Usage: ./nxviewgraph < test_graph.txt

'''
Requirements: networkx, matplotlib
'''

import networkx as nx

# Building a networkx graph from the cluster instance, pnode and snode information.
G = nx.Graph()
while True:
    s = raw_input()
    if s == '':
        break
    l = s.split()
    G.add_edge(l[0],l[1])

# Plotting the graph.
import matplotlib.pyplot as plt
nx.draw(G)
plt.show()
