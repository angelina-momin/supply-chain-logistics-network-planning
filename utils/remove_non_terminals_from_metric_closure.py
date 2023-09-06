from typing import List

import networkx as nx    


def remove_non_terminals_from_metric_closure(metric_closure_graph: nx.Graph, terminal_buildings: List[str])->nx.Graph:
    """
    Removes non terminal nodes and any edges from them from the metric closure graph.
    The resulting graph will only contain terminal nodes.

    Args:
        metric_closure_graph (nx.Graph): Metric closure graph
        terminal_buildings (List[str]): List of the terminal buildings. These always need to connected in the final graph.

    Returns:
        nx.Graph: Graph with only the terminal nodes
    """    
    non_terminal_nodes = [node for node in metric_closure_graph.nodes if metric_closure_graph.nodes[node]['building_type'] not in terminal_buildings]
    metric_closure_graph.remove_nodes_from(non_terminal_nodes)
    return metric_closure_graph