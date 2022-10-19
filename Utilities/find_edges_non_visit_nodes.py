def find_edges_non_visit_nodes(list_edges, list_visited_nodes):
    
    output_list_edges = list()
    
    for edge in list_edges:
        node1, node2 = edge[0], edge[1]
        
        # Both nodes have already been visited
        if node1 and node2 in list_visited_nodes:
            pass
        
        elif node1 or node 2 not in list_visited_nodes:
            ouput_edge.add(edge)
          
        # Both nodes are not a selected node
        else:
            pass
    
    return output_list_edges
    