import os
from typing import Any, Tuple

import networkx as nx
import matplotlib.pyplot as plt

def get_color_node(building_type: str) -> str:
    """
    Returns the color of a node giving the building type.

    Args:
        building_type (str): The building type.

    Returns:
        str: The letter representing the color of the node
    """
    # * Dictionary with keys being the building type and values being the node colors.
    dict_building_node_colors = {
        "factory": "g",  # green
        "warehouse": "r",  # red
        "distribution_center": "b",  # blue
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
        return "0"  # black

    # Express roads (not connecting houses) are colored red.
    return "r"  # red


def create_and_save_graph(
    graph: nx.Graph,
    file_name: str = "graph_visual.png",
    save_file_directory: str = "data/fig/"
) -> None:
    """
    Create and save a graph with nodes and edges colored based on their attributes.

    Args:
        graph (nx.Graph): The graph to be drawn.
        file_name (str): The name of the file where the graph will be saved.
        save_file_directory (str): The directory where the png is to be saved in.

    Returns:
        None
    """

    # * Create directory if it does not exist
    if not os.path.exists(save_file_directory):
        os.makedirs(save_file_directory)

    node_colors = [node['color'] for node in graph.nodes]
    edge_colors = [get_edge_color(edge, graph) for edge in graph.edges]

    nx.draw_networkx(
        graph,
        node_color=node_colors,
        edge_color=edge_colors,
        pos=nx.get_node_attributes(graph, 'pos'),
        with_labels=True,
    )

    # * Save the plot to a file
    plt.savefig(os.path.join(save_file_directory, file_name))
    plt.close()
