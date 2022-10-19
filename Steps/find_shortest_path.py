def find_shortest_path(input_graph, start_node, end_node):
    """
    ---------------
    Input & Output
    ---------------
    
    Input:  
    graph
    start_node
    end_node
    
    set_nodes.  List of nodes that should be present in the graph
    
    Output:  Graph_MST. 
        
    ---------------
    Description
    ---------------
    
    Given a set of nodes (a set of coordinates), returns the MST, Graph_MST, that includes all the nodes.  
    Uses Dijkstra's algorithm.
    
    """
    
    shortest_path = list()
    
    # Step 0) Create list of visited and unvisited nodes.
    
    unvisited_nodes = retrieve_nodes(graph)
    visited_nodes = {}
    
    shortest_path
    
    # Step 1) We start from start node.
    # We take the start_node as the selected_node
    
    selected_node = start_node
    
    unvisited_nodes = remove(selected_node, unvisited_nodes)
    visited_nodes.add(selected_node)
    
    # Step 2) Keep adding shortest paths until we have visited the end_node
    
    while member(end_node, unvisited_nodes):
        
        # Step 2.1) Find all edges from selected_node
        
        # Step 2.2) Choose and add the edge with the minimum weight to the shortest_path
        
        list_edges = find_all_edges_from_node
        
        shortest_edge = lmin
        shortest_path = shortest_path.add(shortest_edge)
        
        # Step 2.3) Find the node that you just visited. Remove this node from the unvisited_nodes
        
        unvisited_nodes.remove(newly_visited_node)
    
    return shortest_path