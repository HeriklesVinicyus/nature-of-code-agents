import networkx as nx
import matplotlib.pyplot as plt

def print_graph(gr):
    G = nx.Graph()
    for i in gr.nodes:
        for j in i:
            G.add_node(j)
    
    for i in gr.nodes:
        for j in i:
            for k in j.nodes_visiveis:
                G.add_edge(k,j)
    
    plt.title("visão do agente")
    nx.draw(G, with_labels=True, node_color='orange', node_size=400, edge_color='black', linewidths=1, font_size=12, pos=nx.spring_layout(G))
    
    plt.show()
