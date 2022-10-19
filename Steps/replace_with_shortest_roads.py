import networkx as nx


def replace_with_shortest_roads(Graph_MST_terminals, Graph_original):

    """
    -------------
    Input & Output
    -------------
    Input: Graph_MST_terminals, Graph_original
    Output: Graph_output

    -------------
    Description
    -------------
    Finds and replaces each edge in Graph_MST_terminals with the shortest path.

    """

    Graph_steiner = nx.Graph()

    # In depth-first-search (DFS) order of MST_terminal finds the shortest
    # path for each edge

    for edge in nx.edge_dfs(Graph_MST_terminals):

        # STEP 0) Identify the nodes connected by the edge
        node1, node2 = edge

        # STEP 1) Find the shortest path between the nodes
        shortest_path = nx.dijkstra_path(Graph_original, node1, node2)

        # STEP 2) Check which nodes in the shortest path are already present in the steiner_tree

        nodes_in_steiner = [node for node in shortest_path if node in Graph_steiner.nodes]

        # STEP 3) Add the entire shortest path

        # Step 3.1) Add the entire path

        if len(nodes_in_steiner) < 2:
            nx.add_path(Graph_steiner, shortest_path)

        # Step 3.2) Add subpath of the shortest path

        else:
            first_node_in_steiner = nodes_in_steiner[0]
            last_node_in_steiner = nodes_in_steiner[-1]

            # Add edges, hence subpaths from:
            # node1 to first_node_in_steiner
            # node2 to last_node_in_steiner

            subpath_before = shortest_path[0:nodes_in_steiner.index(first_node_in_steiner)]
            subpath_after = shortest_path[nodes_in_steiner.index(last_node_in_steiner):len(shortest_path)]

            Graph_steiner.add_path(subpath_before)
            Graph_steiner.add_path(subpath_after)

    return Graph_steiner