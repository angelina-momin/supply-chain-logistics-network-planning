# PACKAGES

import numpy as np
import networkx as nx
import math

from Steps.create_graph_with_roads import create_graph_with_roads
from Steps.create_steiner_tree import create_steiner_tree_roads
from Utilities.change_graph_visuals import color_node, draw_with_color, color_edge

from networkx.algorithms.approximation.steinertree import steiner_tree

# Load utilities and other functions

COST_PER_KM_LOCAL = 1
COST_PER_KM_EXPRESS = 1

# FUNCTION

def city_planning(coords_houses, coords_malls, coords_city_center):
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

    house_nodes_with_coords = { f"H{index}": coords for index, coords in enumerate(coords_houses)}
    mall_nodes_with_coords = { f"M{index}": coords for index, coords in enumerate(coords_malls)}
    center_node_with_coords = { "C": coords_city_center }
    all_nodes_with_coords = house_nodes_with_coords | mall_nodes_with_coords | center_node_with_coords

    first_graph = nx.Graph()

    first_graph.add_nodes_from(list(mall_nodes_with_coords.keys()), building_type="mall")
    first_graph.add_nodes_from(list(house_nodes_with_coords.keys()), building_type="house")
    first_graph.add_node("C", building_type="center")

    nodes_attributes = first_graph.nodes()

    # STEP 0) Create a regular graph with all the possible local_roads and express_roads

    Graph_all_roads = create_graph_with_roads(first_graph, all_nodes_with_coords, COST_PER_KM_LOCAL, COST_PER_KM_EXPRESS)

    # STEP 1) Create a steiner tree
    # Terminal_nodes: all houses, city_centre
    # Optional_nodes: malls

    terminals = list(house_nodes_with_coords.keys() | center_node_with_coords.keys())

    # Creating the steiner tree
    Graph_steiner_tree = create_steiner_tree_roads(Graph_all_roads, terminals)

    ## STEP 2) Visualization

    # Graphs_to_draw = [first_graph, Graph_all_roads, Graph_steiner_tree]
    # map(lambda graph: draw_with_color(graph, all_nodes_with_coords), Graphs_to_draw)
    #print("just before drawing", [(node, Graph_steiner_tree.nodes[node]) for node in Graph_steiner_tree])

    #draw_with_color(steiner_tree(Graph_all_roads, terminals, weight='Distance'), all_nodes_with_coords, nodes_attributes)

    plt.figure().suptitle("Optimal steiner")


    opt_steiner_tree = steiner_tree(Graph_all_roads.copy(), terminals, weight = 'Distance')
    print("optimal weight:", opt_steiner_tree.size("distance"))


    print("Sucky netwrokx steiner", opt_steiner_tree.edges)
    nx.draw_networkx(opt_steiner_tree,
                     node_color=list(map(lambda node: color_node(node, opt_steiner_tree), opt_steiner_tree.nodes)),
                     edge_color=list(map(lambda edge: color_edge(edge, opt_steiner_tree), opt_steiner_tree.edges)),
                     pos=all_nodes_with_coords,
                     with_labels=True
                     )
    plt.figure().suptitle("Rahjeet's and Krishna's optimal tree")

    draw_with_color(
        Graph_steiner_tree,
        n
    )
    print("our shitty weight:", Graph_steiner_tree.size("distance"))


    #draw_with_color(Graph_steiner_tree, all_nodes_with_coords, nodes_attributes)
    plt.show()