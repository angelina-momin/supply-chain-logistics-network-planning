import networkx as nx
from networkx.algorithms.approximation.steinertree import metric_closure

from Steps.replace_with_shortest_roads import replace_with_shortest_roads


def create_steiner_tree_roads(graph, terminals):
    # STEP 1) Create MC of the terminals
    Graph_MC_terminals = metric_closure(graph)

    # Remove non_terminals and all adjacent edges
    non_terminals = [node for node in graph.nodes if node not in terminals]

    Graph_MC_terminals.remove_nodes_from(non_terminals)

    # STEP 2) Create MST of terminal
    Graph_MST_terminals = nx.minimum_spanning_tree(Graph_MC_terminals, algorithm='prim')

    # STEP 3) Find and replace each edge in Graph_MST_terminal with a shortest path.

    steiner_tree = replace_with_shortest_roads(Graph_MST_terminals, graph)

    # the functions above create new graphs, which looses node attribute information
    nx.set_node_attributes(steiner_tree, graph.nodes)

    # print("Steiner_tree", steiner_tree.edges)
    return steiner_tree
