from typing import Dict

import networkx as nx
import math

def create_connected_graph(
    initial_graph_with_nodes: nx.Graph,
    dict_route_costs_per_km: Dict[str, float]
) -> nx.Graph:
    """
    Create a weighted complete graph based on an initial graph with nodes.
    
    Args:
        initial_graph_with_nodes (nx.Graph): Initial graph with nodes, but no edges.
        dict_route_costs_per_km (Dict[str, float]): Dictionary containing the costs for each route type.
        
    Returns:
        nx.Graph: Graph with nodes and weighted edges.
    """

    # * Unpacking costs per km of each road type
    cost_per_km_local_route = dict_route_costs_per_km["local"]
    cost_per_km_express_route = dict_route_costs_per_km["express"]

    # * Looping over each node and creating a weighted edge to every other node
    for source, source_data in initial_graph_with_nodes.nodes(data=True):
        for target, target_data in initial_graph_with_nodes.nodes(data=True):
            
            # We do not create loops or double edges between two nodes
            if source == target or initial_graph_with_nodes.has_edge(source, target):
                continue

            # * Calculating the weight of the edge which is the euclidean distance
            x1, y1 = source_data['pos']
            x2, y2 = target_data['pos']
            eucl_dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            source_type = source_data.get('building_type')
            target_type = target_data.get('building_type')

            # * Adding edges for local roads
            if source_type in ["factory", "warehouse"] and target_type == "factory":
                initial_graph_with_nodes.add_edge(
                    source,
                    target,
                    road="local",
                    weight=eucl_dist * cost_per_km_local_route,
                )

            # * Adding edges for express roads
            elif source_type in ["warehouse", "distribution_center"] and target_type == "warehouse":
                initial_graph_with_nodes.add_edge(
                    source,
                    target,
                    road="express",
                    weight=eucl_dist * cost_per_km_express_route,
                )

    return initial_graph_with_nodes