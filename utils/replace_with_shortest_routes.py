import networkx as nx


def replace_with_shortest_routes(mst_only_terminals_graph: nx.Graph, connected_graph: nx.Graph)->nx.Graph:
    """Replaces the edges in MST with only terminals with the shortest routes.

    Args:
        mst_only_terminals_graph (nx.Graph): The MST graph containing only the terminals.
        connected_graph (nx.Graph): The connected graph which contains all possible roads.

    Returns:
        nx.Graph: The steiner graph, which is the solution to the problem.
    """

    steiner_graph = nx.Graph()

    # * We depth-first-search (DFS) order of MST_terminal finds the shortest path for each edge
    for node1, node2 in nx.edge_dfs(mst_only_terminals_graph):

        # *Find the shortest path between the nodes
        # We use the original connected graph to find the shortest path
        shortest_path = nx.dijkstra_path(connected_graph, node1, node2)

        # * Check which nodes in the shortest path are already present in the steiner_tree
        # We check which nodes are there in the steiner_graph
        nodes_in_shortest_path_and_steiner = [node for node in shortest_path if node in steiner_graph.nodes]

        # * Adding the entire shortest path to the steiner graph
        # Only one or no nodes of the shortest path are in the steiner graph so we add the entire shortest 
        # path to the graph. 
        if len(nodes_in_shortest_path_and_steiner) < 2:
            nx.add_path(steiner_graph, shortest_path)

        # * Add subpath of the shortest path
        # If there are two vertices already in the tree adding the path will result in cycles. So we only 
        # add subpaths from the terminals to the vertices already in the tree. This ensure cycles are avoided
        # and the terminals are included.
        else:
            first_node_in_steiner = nodes_in_shortest_path_and_steiner[0]
            last_node_in_steiner = nodes_in_shortest_path_and_steiner[-1]

            # Add edges, hence subpaths from node1 to first_node_in_steiner
            subpath_before = shortest_path[:shortest_path.index(first_node_in_steiner) + 1]

            # Add edges, hence subpaths from last_node_in_steiner to node2
            subpath_after = shortest_path[shortest_path.index(last_node_in_steiner):]

            nx.add_path(steiner_graph, subpath_before)
            nx.add_path(steiner_graph, subpath_after)

    return steiner_graph
