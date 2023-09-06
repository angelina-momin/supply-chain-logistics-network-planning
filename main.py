# PACKAGES

import numpy as np
import networkx as nx
from networkx.algorithms.approximation.steinertree import steiner_tree
from networkx.algorithms.approximation.steinertree import metric_closure
import math

from utilities.create_connected_graph import create_connected_graph
from utilities.initialize_graph_with_nodes import initialize_graph_with_nodes
from utilities.remove_non_terminals_from_metric_closure import remove_non_terminals_from_metric_closure
from Steps.create_steiner_tree import create_steiner_tree_roads


# Load utilities and other functions
dict_route_costs_per_km = {"local": 5, "express": 1}

def city_planning(
    list_factory_coords: np.ndarray,
    list_warehouse_coords: np.ndarray,
    list_distribution_center_coords: np.ndarray,
):
    """
    ---------------
    Input & Output
    ---------------
    
    Input:     
    coords_houses- set of housing coordinates
    coords_malls- set of mall coordinates
    coords_city_center- city central coordinates
    
    Output:
    steiner_tree- networkx graph which is a list of nodes and edges along with their weights
    visual_steiner_tree- visualization of the steiner tree
    
    ---------------
    Description
    ---------------
    
    Creates urban planning with roads connecting houses, city center and optionally malls such that 
    the total weight of the network, hence the construction costs are minimized. 
    
    The function essentially creates a Steiner tree with:
        - Terminal node set = all houses and the city center
        - Steiner node set (optional nodes) = all malls
    
    ---------------
    Variables
    ---------------
    
    """
    terminal_buildings = ["distribution_center", "factory"]

    initial_graph = initialize_graph_with_nodes(list_factory_coords, list_warehouse_coords, list_distribution_center_coords)

    # * Creating a graph with all possible roads
    connected_graph = create_connected_graph(initial_graph, dict_route_costs_per_km)

    # * Creating metric closure of the connected graph
    # The metric closure of the connected graph is a complete graph where each edge which each edge is weighted by the 
    # shortest path distance between the nodes in the connected graph
    metric_closure_graph = metric_closure(connected_graph)

    # * Removing all non-terminal nodes from the metric closure graph
    metric_closure_graph_only_terminals = remove_non_terminals_from_metric_closure(metric_closure_graph, terminal_buildings)

    # STEP 1) Create a steiner tree
    # Terminal_nodes: all houses, city_centre
    # Optional_nodes: malls

    terminals = list(house_nodes_with_coords.keys() | center_node_with_coords.keys())

    # Creating the steiner tree
    Graph_steiner_tree = create_steiner_tree_roads(connected_graph, terminals)

    ## STEP 2) Visualization
    #plt.figure(figsize=(40, 40)).suptitle("Rahjeet's and Krishna's optimal tree")
    draw_with_color(Graph_steiner_tree, all_nodes_with_coords, nodes_attributes)

    # plt.set_xticks(range(0, 200))
    # plt.set_yticks(range(0, 200))

    plt.show()