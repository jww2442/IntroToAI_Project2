import networkx as nx
import matplotlib.pyplot as plt


def get_color(val):
    if(val == 0):
        return 'white'
    if(val == 1):
        return 'red'
    if(val == 2):
        return 'blue'
    if(val == 3):
        return 'yellow'
    if(val == 4):
        return 'green'
    print('error 529')

def print_graph1(points, edges, assignments):
    G = nx.Graph()
    for i in range(len(points)):
        G.add_node(i)

    for e in edges:
        G.add_edge(e[0], e[1])

    cols = []
    for c in assignments:
        cols.append(get_color(c))
    
    nx.draw(G, node_color=cols, with_labels=True, font_weight='bold')

    #nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    plt.show()


