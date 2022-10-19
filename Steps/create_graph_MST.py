def create_graph_MST(input_graph, city_center):
    """
    ---------------
    Input & Output
    ---------------
    
    Input:  input_graph. The MST is to be created from this input_graph.
    
    Output:  Graph_MST. A networkX graph that consists of nodes and edges.
        
    ---------------
    Description
    ---------------
    
    Uses Prim's algorithm to generate a MST graph, Graph_MST, from the input graph, input_graph.
    
    """
    
    # Step 0) Generating output graph, Graph_MST
    # Creating set of visited nodes, set_visited_nodes
    
    Graph_MST = nx.Graph()
    set_visited_nodes = {}
    
    all_nodes = nodes_retrieved_Graph_MST # Collecting the nodes in the grpah
    
    # Step 1) Choose an initial node to start the algorithm from.
    # We always choose the city center to be our start.
    
    selected_node = city_center
    set_visited_nodes = set_visited_nodes.add(city_center)
    
    # Step 2) Add edges  While set_visited_nodes != all_graph_nodes do:
    
    while set_visited_nodes != all_graph_nodes:
    
        # Step 2.1) Find all the edges connecting a node from set_visited_nodes to a node not in set_visited_nodes
        
        edges_non_visited_nodes = find_edges_non_visited_nodes(list_edges, list_visited_nodes)
        
        # Step 2.2) Of all the edges, find and select the edge with the minimum weight.
               
        edge_min_weight = pick_edge_min_weight(edges_non_visited_nodes)
        
        # Step 2.3) Add this edge to Graph_MST
        
        Graph_MST.add_weighted_edges_from(edge_min_weight)
                                          
        # Step 2.4) Add the newly visited node (node that was not in set_visited_nodes) to set_visited_nodes
                                          
        set_visited_nodes.add(newly_visit_node)
    
    return Graph_MST                                      
                                    