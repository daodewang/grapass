# analysis the grapass of cellphone

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

N = 2001
M = 8000

G = nx.generators.random_graphs.gnm_random_graph(N,M)
while(nx.algorithms.connectivity.edge_augmentation.is_k_edge_connected(G,1) == False):
    print('gen G')
    G = nx.generators.random_graphs.gnm_random_graph(N, M)
nx.draw(G)
plt.show()

betweeness = nx.algorithms.centrality.betweenness_centrality(G)
print(betweeness)
T = 0
for v in betweeness.values():
    T += v

avlen = nx.algorithms.shortest_paths.generic.average_shortest_path_length(G)
print(avlen)
print(T)




"""
a b c
d e f
g h i
"""

"""
a c i g b d f h e



neib = [[0,0,0,0,1,1,0,0,1],
        [0,0,0,0,1,0,1,0,1],
        [0,0,0,0,0,0,1,1,1],
        [0,0,0,0,0,1,0,1,1],
        [1,1,0,0,0,1,1,0,1],
        [1,0,0,1,1,0,0,1,1],
        [0,1,1,0,1,0,0,1,1],
        [0,0,1,1,0,1,1,0,1],
        [1,1,1,1,1,1,1,1,0]]

m = np.array(neib)

print(m)

print(m*m)
"""
