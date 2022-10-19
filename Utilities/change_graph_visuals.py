import networkx as nx

def color_node(node, graph):
    node_attrs = graph.nodes[node]

    print("color node", [(node, graph.nodes[node]) for node in graph])

    if "building_type" not in node_attrs:
        print(node, node_attrs)
        print(node_attrs["building_type"])


    if node_attrs["building_type"] == "house":
        return '0' # black
    elif node_attrs["building_type"] == "mall":
        return 'r' # red
    else:
        return 'b' # blue


def color_edge(edge, graph):
    node1, node2 = edge

    node1_attr, node2_attr = graph.nodes[node1], graph.nodes[node2]

    # Local roads (H-H, H-M) are colored black.
    if node1_attr["building_type"] == "house" or node2_attr["building_type"] == "house":
        return '0' # black

    # Express roads (M-M, M-C) are colored red.
    else:
        return 'r' # red


def draw_with_color(graph, nodes_coords, nodes_attributes):
    print("graph to draw", [(node, graph.nodes[node]) for node in graph])
    graph.add_nodes_from(list(nodes_coords.keys()))
    nx.set_node_attributes(graph, nodes_attributes)
    nx.draw_networkx(
        graph,
        node_color= list(map(lambda node: print("we have the node", graph.nodes[node]), graph.nodes)),
        edge_color= list(map(lambda edge: color_edge(edge, graph), graph.edges)),
        pos = nodes_coords
    )
