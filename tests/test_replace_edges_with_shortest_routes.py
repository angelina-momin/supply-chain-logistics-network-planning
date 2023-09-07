import networkx as nx
from networkx.algorithms.approximation.steinertree import metric_closure

from utils.replace_edges_with_shortest_routes import replace_edges_with_shortest_routes 

def test_replace_edges_with_shortest_routes_basic_graph():

    # * Create a connected graph with all possible roads
    connected_graph = nx.Graph()
    connected_graph.add_edge(1, 2, weight=1)
    connected_graph.add_edge(2, 3, weight=1)
    connected_graph.add_edge(1, 3, weight=10)  # Longer route which will not be included in the final graph

    # * Create a simple MST graph with only terminals
    mst_graph = metric_closure(connected_graph)

    # * Call the function
    steiner_graph = replace_edges_with_shortest_routes(mst_graph, connected_graph)

    assert steiner_graph.has_edge(1, 2)
    assert steiner_graph.has_edge(2, 3)
    assert not steiner_graph.has_edge(1, 3)  # This edge should not be present since it's a longer route
