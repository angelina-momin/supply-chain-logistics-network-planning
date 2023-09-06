# PACKAGES

import numpy as np
import networkx as nx
from networkx.algorithms.approximation.steinertree import steiner_tree
from networkx.algorithms.approximation.steinertree import metric_closure
import math

from utils.create_connected_graph import create_connected_graph
from utils.initialize_graph_with_nodes import initialize_graph_with_nodes
from utils.remove_non_terminals_from_metric_closure import remove_non_terminals_from_metric_closure
from utils.replace_edges_with_shortest_routes import replace_edges_with_shortest_routes
from utils.graph_visualization import create_and_save_graph

# Load utilities and other functions
dict_route_costs_per_km = {"local": 5, "express": 1}

def suppy_chain_network_planning(
    list_factory_coords: np.ndarray,
    list_warehouse_coords: np.ndarray,
    list_distribution_center_coords: np.ndarray,
    figure_filename: str = "graph_visual.png",
    save_file_directory: str = "data/fig/"
)-> None:
    """
    Solves the supply chain network planning problem given a list of coords of factory, warehouse and distribution
    center coords.

    Args:
        list_factory_coords (np.ndarray): Array containing the coordinates of factories.
        list_warehouse_coords (np.ndarray): Array containing the coordinates of warehouses.
        list_distribution_center_coords (np.ndarray): Array containing the coordinates of distribution centers.
        figure_filename (str): The name of the file where the Steiner tree will be visualized and saved.
        save_file_directory (str): The directory where the png is to be saved in.

    Returns:
        None
    """
    terminal_buildings = ["distribution_center", "factory"]

    initial_graph = initialize_graph_with_nodes(list_factory_coords, list_warehouse_coords, list_distribution_center_coords)

    # * Creating a graph with all possible roads
    connected_graph = create_connected_graph(initial_graph, dict_route_costs_per_km)

    # * Creating metric closure of the connected graph
    # The metric closure of the connected graph is a complete graph where each edge is weighted by the 
    # shortest path distance between the nodes in the connected graph
    metric_closure_graph = metric_closure(connected_graph)
    # * Copying node attributes
    # The functions above create graphs without the node attributes
    nx.set_node_attributes(metric_closure_graph, connected_graph.nodes)

    # * Removing all non-terminal nodes from the metric closure graph
    metric_closure_only_terminals_graph = remove_non_terminals_from_metric_closure(metric_closure_graph, terminal_buildings)

    # * Creating minimum spanning tree (MST) of the terminal nodes
    # The MST will connect all the terminal nodes without any cycles and minimum possible total edge weight
    mst_only_terminals_graph = nx.minimum_spanning_tree(metric_closure_only_terminals_graph, algorithm='prim')

    # * Replaces the edges of the MST with the shortest routes    
    steiner_tree_graph = replace_edges_with_shortest_routes(mst_only_terminals_graph, connected_graph)

    # * Create and save visualization
    create_and_save_graph(steiner_tree_graph, figure_filename, save_file_directory)
