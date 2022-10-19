
def color_node(node):
    if node["type"] == "house":
        return '0' # black
    elif node["type"] == "mall":
        return 'r'
    else node["type"] == "center":
        return 'b'


def color_edge(edge):

    node1[0], node2[1] = edge[0], edge[1]

    # Local roads (H-H, H-M) are colored black.
    if node1["type"] == "house" or node2["type"] == "house":
        return '0' # black

    # Express roads (M-M, M-C) are colored red.
    else:
        return 'r'


def draw_with_color(graph, nodes_coords):
    nx.draw_networkx(
        graph,
        node_color=map(color_node, Graph_all_roads.nodes),
        edge_color=map(color_edge, Graph_all_roads.edges),
        pos = nodes_coords
    )