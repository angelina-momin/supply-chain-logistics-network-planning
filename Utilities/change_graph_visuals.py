import networkx as nx

def color_node(node, graph):
    node_attrs = graph[node]

    if "building_type" not in node_attrs:
        print(node, node_attrs)
    if node_attrs["building_type"] == "house":
        return '0' # black
    elif node_attrs["building_type"] == "mall":
        return 'r' # red
    else:
        return 'b' # blue


def color_edge(edge, graph):
    node1, node2 = edge

    node1_attr, node2_attr = graph[node1], graph[node2]

    # Local roads (H-H, H-M) are colored black.
    if node1_attr["building_type"] == "house" or node2_attr["building_type"] == "house":
        return '0' # black

    # Express roads (M-M, M-C) are colored red.
    else:
        return 'r' # red


def draw_with_color(graph, nodes_coords):
    nx.draw_networkx(
        graph,
        node_color= list(map(lambda node: color_node(node, graph), graph.nodes)),
        edge_color= list(map(lambda edge: color_edge(edge, graph), graph.edges)),
        pos = nodes_coords
    )