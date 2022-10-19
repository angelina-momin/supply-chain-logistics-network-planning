import networkx as nx
import math

from main import COST_PER_KM_LOCAL, COST_PER_KM_EXPRESS


def create_graph_with_roads(graph):
    """
    ---------------
    Input & Output
    ---------------
    
    Input:  
    set_HC- set of housing coordinates (HC)
    set_MC- set of mall coordinates (MC)
    set_CC- city central coordinates (CC)
    
    cost_km_LR- cost per km of local roads
    cost_km_ER- cost per km of express roads
    
    Output:  Graph_all_roads.  Graph consisting of all the nodes with edges 
    of edge_weight = euclidean distance * cost_per_km of the specific road type
        
    ---------------
    Description
    ---------------
    
    Given a set of nodes (a set of coordinates), returns a complete graph, Graph_all_roads.
    A complete graph has an edge between every two vertices.
    
    Weight of each edge = euclidean distance between the nodes.
    
    ---------------
    Notes
    ---------------
    
    The metric closure of a graph G is:
    
    1) a complete graph with
    2) each edge's weight = shortest path distance between the nodes in G.
    
    This function creates a metric closure graph because the output graph is:
    1) a complete graph
    2) each edge's weight = Euclidean distance = shortest path distance between the nodes.
    
    """

    # Step 0) Generating output graph, Graph_all_roads

    Graph_all_roads = graph.copy()

    # Step 1 oles suggestion
    for source in Graph_all_roads.nodes:
        for destination in Graph_all_roads.nodes:
            if Graph_all_roads.has_edge(source, destination):
                continue

            ## Step 2.2) Calculating the road_weight
            # Edge weight = euclidean distance * cost_road_type

            x1, y1 = source[0], source[1]
            x2, y2 = destination[0], destination[1]

            # Calculating euclidean distance
            eucl_dist = math.sqrt((x2 - x1) ^ 2 + (y2 - y1) ^ 2)

            if source.type == "mall" and destination.type == "mall":
                Graph_all_roads.add_edge(source, destination, road="express", weight=eucl_dist * COST_PER_KM_LOCAL)
            else:
                Graph_all_roads.add_edge(source, destination, road="local", weight=eucl_dist * COST_PER_KM_EXPRESS)

    return Graph_all_roads
