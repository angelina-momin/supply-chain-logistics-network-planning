from typing import List, Tuple

import networkx as nx


def replace_with_shortest_routes(
    mst_only_terminals_graph: nx.Graph, connected_graph: nx.Graph
) -> nx.Graph:
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
        nodes_in_shortest_path_and_steiner = [
            node for node in shortest_path if node in steiner_graph.nodes
        ]

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
            first_common_node = nodes_in_shortest_path_and_steiner[0]
            last_common_node = nodes_in_shortest_path_and_steiner[-1]

            subpath_to_first_common_node, subpath_from_last_common_node = find_subpaths(
                shortest_path, first_common_node, last_common_node
            )

            nx.add_path(steiner_graph, subpath_to_first_common_node)
            nx.add_path(steiner_graph, subpath_from_last_common_node)

    return steiner_graph


def find_subpaths(
    shortest_path: List[int], first_common_node: int, last_common_node: int
) -> Tuple[List[int], List[int]]:
    """
    Find the subpaths in a shortest path that extend to the first and last common nodes in steiner

    Args:
        shortest_path (List[int]): The list of nodes representing the shortest path.
        first_common_node (int): The first node that is common between the shortest path and some set of existing nodes.
        first_common_node (int): The last node that is common between the shortest path and some set of existing nodes.

    Returns:
        Tuple[List[int], List[int]]: Two lists representing the subpaths to the first and from the last common nodes.
    """

    # * Find subpath from node1 in shortest_path to first_node_in_steiner
    subpath_to_first = shortest_path[: shortest_path.index(first_common_node) + 1]
    # * Find subpath from from last_node_in_steiner to node2 in shortest path
    subpath_from_last = shortest_path[shortest_path.index(last_common_node) :]

    return subpath_to_first, subpath_from_last
