from Steps.create_graph_with_roads import create_graph_with_roads
from Steps.create_graph_MC import create_graph_MC
from Steps.create_graph_MST import create_graph_MST

from Steps.replace_with_shortest_roads import replace_with_shortest_roads


def create_steiner_tree_roads(graph, terminals):
    # Creating all graphs
    Graph_all_roads = nx.Graph()
    Graph_MC_terminal = nx.Graph()
    Graph_MST_terminal = nx.Graph()

    # STEP 1) Create a graph with all possible roads (which follows all rules)
    Graph_all_roads = create_graph_with_roads(graph)

    # STEP 2) Create MC of the terminals
    Graph_MC_terminals = nx.metric_closure(Graph_all_roads, terminals)

    # Remove non_terminals and all adjacent edges
    non_terminals = [node for node in Graph_all_roads.nodes if node not in terminals]

    Graph_MC_terminals = nx.remove_nodes_from(non_terminals)

    # STEP 3) Create MST of terminal
    Graph_MST_terminals = nx.minimum_spanning_tree(Graph_MC_terminal, algorithm='prim')

    # STEP 4) Find and replace each edge in Graph_MST_terminal with a shortest path.

    steiner_tree = replace_with_shortest_roads(Graph_MST_terminals, Graph_all_roads)

    return steiner_tree
