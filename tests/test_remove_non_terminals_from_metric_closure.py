import networkx as nx

from utils.remove_non_terminals_from_metric_closure import remove_non_terminals_from_metric_closure  


def test_remove_non_terminals_from_metric_closure():
    
    # * Create a sample metric closure graph
    metric_closure_graph = nx.Graph()
    metric_closure_graph.add_node(1, building_type="terminal")
    metric_closure_graph.add_node(2, building_type="non-terminal")
    metric_closure_graph.add_node(3, building_type="terminal")
    metric_closure_graph.add_edge(1, 2)
    metric_closure_graph.add_edge(2, 3)
    metric_closure_graph.add_edge(1, 3)

    terminal_buildings = ["terminal"]

    result_graph = remove_non_terminals_from_metric_closure(metric_closure_graph, terminal_buildings)

    # * Assertions
    assert 1 in result_graph.nodes
    assert 3 in result_graph.nodes
    assert 2 not in result_graph.nodes  # This non-terminal node should be removed

    assert result_graph.has_edge(1, 3)
    # The following edges from non-terminal node 2 should be removed
    assert not result_graph.has_edge(1, 2)  
    assert not result_graph.has_edge(2, 3)  