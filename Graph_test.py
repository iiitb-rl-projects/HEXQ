import networkx as nx
import matplotlib.pyplot as plt

'''
g=nx.Graph()
g.add_node(2)
g.add_node(5)

g.add_edge(2,5)
g.add_edge(4,1)
g.add_edges_from([(1,2),(3,4)])


print nx.info(g)

nx.draw(g)

plt.show()
'''

g=nx.DiGraph()

#for i in range (25):
#    g.add_node(i)
#    g.add_edge(i,i)
edge_list=[(0,1),(1,0),(2,3),(3,2),(3,4),(4,3),(5,6),(6,5),(7,8),
           (8,7),(8,9),(9,8),(10,11),(11,10),(11,12),(12,11),(12,13,),
           (13,12),(13,14),(14,13),(16,17),(17,16),(18,19),(19,18),(21,22),
           (22,21),(23,24),(24,23),(0,5),(5,0),(1,6),(6,1),(2,7),(7,2),(3,8),
           (8,3),(4,9),(9,4),(5,10),(10,5),(6,11),(11,6),(7,12),(12,7),(8,13),
           (13,8),(9,14),(14,9),(10,15),(15,10),(11,16),(16,11),(12,17),(17,12),(13,18),(18,13),(14,19),
           (19,14),(15,20),(20,15),(16,21),(21,16),(17,22),(22,17),(18,23),
           (23,18),(19,24),(24,19)]
g.add_edges_from(edge_list)
g.nodes_with_selfloops()
print nx.info(g)
#print nx.strongly_connected_components(g)

print [len(c) for c in sorted(nx.strongly_connected_components(g),
                        key=len, reverse=True)]

nx.draw(g, with_labels=True)

plt.show()


