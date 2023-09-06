from typing import Any, Dict, Tuple, Union

import networkx as nx

def get_color_node(building_type: str)-> str:
    """
    Returns the color of a node giving the building type.

    Args:
        building_type (str): The building type.

    Returns:
        str: The letter representing the color of the node
    """
    # * Dictionary with keys being the building type and values being the node colors.
    dict_building_node_colors = {
        "factory": "g", # green
        "warehouse": "r", # red
        "distribution_center": "b" # blue
    }

    # * Raising error if node does not have building_type attribute
    if building_type not in dict_building_node_colors.keys():
        raise KeyError(f"Unrecognized building type has been passed: {building_type}.")
    
    # * Returning the associated color
    return dict_building_node_colors["building_type"]

def get_edge_color(edge: Tuple[Any, Any], graph: nx.Graph) -> str:
    """
    Determine the color of an edge based on the building types of its nodes.

    Args:
        edge (Tuple[Any, Any]):
        graph (nx.Graph): The graph.

    Returns:
        str: Color code ('0' for black or 'r' for red).
    """
    node1, node2 = edge

    node1_attr, node2_attr = graph.nodes[node1], graph.nodes[node2]

    # Local roads (connecting house and house or house and mall) are colored black.
    if node1_attr["building_type"] == "house" or node2_attr["building_type"] == "house":
        return '0' # black

    # Express roads (not connecting houses) are colored red.
    return 'r' # red


def draw_colored_graph(graph: nx.Graph, nodes_coords: Dict[Any, Tuple[float, float]], nodes_attributes: Dict[Any, Dict[str, Union[str, Any]]]) -> None:
    """
    Draw a graph with colored nodes and edges based on their attributes.

    Args:
        graph (nx.Graph): The graph to be drawn.
        nodes_coords (Dict[Any, Tuple[float, float]]): Dictionary mapping nodes to their coordinates (x, y).
        nodes_attributes (Dict[Any, Dict[str, Union[str, Any]]]): Dictionary mapping nodes to their attributes.

    Returns:
        None
    """

    graph.add_nodes_from(list(nodes_coords.keys()))
    nx.set_node_attributes(graph, nodes_attributes)
    
    nx.draw_networkx(
        graph,
        node_color= list(map(lambda node: get_color_node(node, graph), graph.nodes)),
        edge_color= list(map(lambda edge: get_edge_color(edge, graph), graph.edges)),
        pos = nodes_coords,
        with_labels = True
    )
