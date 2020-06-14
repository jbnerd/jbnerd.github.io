import networkx as nx
from networkx.drawing.nx_agraph import to_agraph 


if __name__ == "__main__":
    g = nx.MultiGraph()
    g.add_edge(1, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    nx.draw(g)
    A = to_agraph(g)
    A.layout('circo')
    A.draw('bridges_of_konigsberg.png')
