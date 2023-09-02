import numpy as np
import networkx as nx

def initialize_graph_with_nodes(list_factory_coords: np.ndarray, list_warehouse_coords: np.ndarray, list_distribution_center_coords: np.ndarray)->nx.Graph:
    """
    Given building coords, initializes and returns a networkx graph with the nodes for each building.
    The nodes contains information on the coords as well as the building types.

    Args:
        list_factory_coords (np.ndarray): List of factory coords
        list_warehouse_coords (np.ndarray): List of warehouse coords
        list_distribution_center_coords (np.ndarray): List of distribution center coords

    Returns:
        nx.Graph: A networkx graph containing all the nodes
    """   

    factory_nodes = { f"F{index}": coords for index, coords in enumerate(list_factory_coords)}
    warehouse_nodes = { f"W{index}": coords for index, coords in enumerate(list_warehouse_coords)}
    distribution_center_node = { "DC": list_distribution_center_coords }
    all_nodes = factory_nodes | warehouse_nodes | distribution_center_node

    # * Initialize graph
    network_graph = nx.Graph()

    # Add nodes with their attributes
    for node, coords in all_nodes.items():
        if node == "DC":
            building_type = "distribution center"
        elif node.startswith("W"):
            building_type = "warehouse"
        else:
            building_type = "factory"

        network_graph.add_node(node, pos=coords, building_type=building_type)

    return network_graph
