import networkx as nx
import math

def create_connected_graph(
    initial_graph_with_nodes: nx.Graph,
    cost_per_km_local_road: float,
    cost_per_km_express_road: float,
) -> nx.Graph:
    """
    Create a weighted complete graph based on an initial graph with nodes.
    
    Args:
        initial_graph_with_nodes (nx.Graph): Initial graph with nodes, but no edges.
        cost_per_km_local_road (float): Cost per km of local roads.
        cost_per_km_express_road (float): Cost per km of express roads.
        
    Returns:
        nx.Graph: Graph with nodes and weighted edges.
    """

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
                    weight=eucl_dist * cost_per_km_local_road,
                )

            # * Adding edges for express roads
            elif source_type in ["warehouse", "distribution_center"] and target_type == "warehouse":
                initial_graph_with_nodes.add_edge(
                    source,
                    target,
                    road="express",
                    weight=eucl_dist * cost_per_km_express_road,
                )

    return initial_graph_with_nodes