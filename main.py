# PACKAGES

import numpy as np
import networkx as nx
import math

from itertools import product

from Steps.create_graph_with_roads import create_graph_with_roads


# Load utilities and other functions

COST_PER_KM_LOCAL = 1
COST_PER_KM_EXPRESS = 1

# FUNCTION

def city_planning(set_houses, set_malls, set_city_center):
    """
    ---------------
    Input & Output
    ---------------
    
    Input:     
    set_houses- set of housing coordinates
    set_malls- set of mall coordinates
    set_city_center- city central coordinates 
    
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

    # I dunno angelina
    first_graph = nx.Graph()
    first_graph.add_nodes_from(set_houses, type="house")
    first_graph.add_nodes_from(set_malls, type="mall")
    first_graph.add_nodes_from(set_city_center, type="center") # TODO city center is not a set

    
    set_nodes = union(set_houses, set_malls, set_city_center)
    set_terminal_nodes = union(set_houses, set_city_center)
    
    # All the graphs we need
    Graph_all_roads = nx.Graph()
    Graph_MC_terminal = nx.Graph()
    Graph_MST_terminal= nx.Graph()
    Graph_steiner_tree = nx.Graph()

    # Empty list containing all graphs

    all_graphs = {}

    # STEP 0) Create a regular graph with all the possible local_roads and express_roads
    
    Graph_all_roads = create_graph_with_roads(set_nodes)

    # STEP 1) Create a steiner tree
    # Terminal_nodes: all houses, city_centre (and hence atleast one mall to connect to the city center)
    # Optional_nodes: malls

    terminal_nodes = union(set_houses, set_city_center)
    optional_nodes = set_malls

    # Setting up the terminal and non terminal nodes
    all_nodes = union(selected_mall, set_houses, set_mall, city_center)
    terminal_nodes = union(set_houses, selected_mall)

    # Creating the steiner tree
    Graph_steiner_tree = create_steiner_tree(terminals, optionals)

    ## STEP 2) Visualization
    
    nx.draw_networkx(Graph_all_roads)
    nx.draw(Graph_MC_terminal)
    nx.draw(Graph_MST_terminal)
    nx.draw(Graph_steiner_tree)
    
    return(Graph_steiner_tree)
