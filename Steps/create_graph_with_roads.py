import networkx as nx
import math


def create_graph_with_roads(graph, coordinates, cost_km_LR, cost_km_ER):
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
    of edge_weight = euclidean distance * cost_per_km of the specific road building_type
        
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
            if source == destination or Graph_all_roads.has_edge(source, destination):
                continue

            ## Step 2.2) Calculating the road_weight
            # Edge weight = euclidean distance * cost_road_type
            source_coordinate = coordinates[source]
            destination_coordinate = coordinates[destination]

            x1, y1 = source_coordinate[0], source_coordinate[1]
            x2, y2 = destination_coordinate[0], destination_coordinate[1]

            # Calculating euclidean distance
            eucl_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            source_attrs = Graph_all_roads.nodes[source]
            destination_attrs = Graph_all_roads.nodes[destination]

            house_and_house = source_attrs["building_type"] == "house" and destination_attrs["building_type"] == "house"
            house_and_mall = source_attrs["building_type"] == "house" and destination_attrs["building_type"] == "mall"
            mall_and_house = source_attrs["building_type"] == "mall" and destination_attrs["building_type"] == "house"
            mall_and_mall = source_attrs["building_type"] == "mall" and destination_attrs["building_type"] == "mall"
            mall_and_center = source_attrs["building_type"] == "mall" and destination_attrs["building_type"] == "center"
            center_and_mall = source_attrs["building_type"] == "center" and destination_attrs["building_type"] == "mall"

            if mall_and_mall or mall_and_center or center_and_mall:
                Graph_all_roads.add_edge(source, destination, road="express", weight=eucl_dist * cost_km_ER)

            elif house_and_house or house_and_mall or mall_and_house:
                Graph_all_roads.add_edge(source, destination, road="local", weight=eucl_dist * cost_km_LR)

    return Graph_all_roads
