def find_all_edges_from_node(list_edges, input_node):
    
    list_edges = {}
    
    for edge in list_edges:
        node1, node2 = edge[0], edge[1]
        
        if node1 == input_node or node2 == input_node :
            list_edges.add(edge)
        
        else:
            pass
        
    return list_edges