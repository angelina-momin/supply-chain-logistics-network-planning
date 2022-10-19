# PACKAGES

import numpy as np
import networkx as nx
import math

from itertools import product

# FUNCTION

def city_planning(set_HC, set_MC, CC):
    """
    ---------------
    Input & Output
    ---------------
    
    Input:     
    set_HC- set of housing coordinates
    set_MC- set of mall coordinates
    CC- city central coordinates 
    
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
    
    set_nodes = union(set_HC, set_MC, CC)
    set_terminal_nodes = union(set_HC, CC)
    
    # All the graphs we need
    Graph_all_roads = nx.Graph()
    Graph_MC_terminal = nx.Graph()
    Graph_MST_terminal= nx.Graph()
    Graph_steiner_tree = nx.Graph()
    
    # STEP 0) Create graph containing all roads, Graph_all_roads
    
    Graph_all_roads =  create_graph_with_roads(set_nodes)

    # STEP 1) Construct a metric closure, Graph_MC_terminal, including only the terminal nodes
    # We can use the function create_graph_with_roads again for this, the only difference being,
    # we use the input set_terminal_nodes
    
    Graph_MC_terminal = create_graph_with_roads(set_terminal_nodes)

    # STEP 2) Find an MST, Graph_MST_terminal, of the graph containing only the terminal nodes. 
    # Graph_MST_terminal is generated from Graph_MC_terminal
    
    Graph_MST_terminal = create_MST(Graph_MC_terminal)

    # STEP 3) Find and replace each edge in Graph_MST_terminal with a shortest path.
    
    # Do, in depth-first-search (DFS) order of MST_terminal
    # For each edge, E = edge(node1, node2), find the shortest path
    
    for edge in MST_terminal:
        node1, node2 = edge
        shortest_path = find_shortest_path(node1, node2)
        
        # Members of the shortest_path already present in steiner_tree
        nodes_in_steiner = member(shortest_path, steiner_tree)
        
        # STEP 3.1) Add the entire shortest path
        
        if length(nodes_in_steiner) < 2 
            steiner_tree.add_edge(shortest_path)
    
        # STEP 3.2) Add subpath of the shortest path
        
        else:
            first_node_in_steiner, last_node_in_steiner = nodes_in_steiner[0], nodes_in_steiner[n]
            
            # Add edges, hence subpaths from:
                # node1 to first_node_in_steiner
                # node2 to last_node_in_steiner
            
            steiner_tree.add_edge(node1, first_node_in_steiner)
            steiner_tree.add_edge(node2, last_node_in_steiner)        
        
            
    ## STEP 5) Create visualization
    
    nx.draw(Graph_all_roads)
    nx.draw(Graph_MC_terminal)
    nx.draw(Graph_MST_terminal)
    nx.draw(steiner_tree)
    
    return(steiner_tre)
