def create_graph_with_roads(set_HC, set_MC, set_CC, cost_km_LR, cost_km_ER):
    
    """
    ---------------
    Input & Output
    ---------------
    
    Input:  
    set_HC- set of housing coordinates (HC)
    set_MC- set of mall coordinates (MC)
    set_CC- city central coordinates (CC)
    
    cost_km_LR- cost per km of local roads
    cost_km_ER- cost per km of express roads
    
    Output:  Graph_all_roads.  Graph consisting of all the nodes with edges 
    of edge_weight = euclidean distance * cost_per_km of the specific road type
        
    ---------------
    Description
    ---------------
    
    Given a set of nodes (a set of coordinates), returns a complete graph, Graph_all_roads.
    A complete graph has an edge between every two vertices.
    
    Weight of each edge = euclidean distance between the nodes.
    
    ---------------
    Notes
    ---------------
    
    The metric closure of a graph G is:
    
    1) a complete graph with
    2) each edge's weight = shortest path distance between the nodes in G.
    
    This function creates a metric closure graph because the output graph is:
    1) a complete graph
    2) each edge's weight = Euclidean distance = shortest path distance between the nodes.
    
    """
    
    # Step 0) Generating output graph, Graph_all_roads
    
    Graph_all_roads = nx.Graph()
    
    # Step 1) Generating edges (without weight) by creating pairings of nodes.
    
        # Cartesian product of nodes- Creating pairings of nodes.
        # Each node is connected to every other node in set_nodes.
        
        # Local roads pais
        roads_HH = list(product(set_HC, set_HC))
        roads_HM = list(product(set_HC, set_MC))
        
        roads_local = union(pairs_HH, pairs_HM)       
        
        # Express roads pairs
        roads_MM = list(product(set_MC, set_MC))
        roads_MC = list(product(set_CC, set_CC))
        
        roads_express = union(pairs_MM, pairs_MC) 
        
        # List of all roads
        
        all_roads = union(roads_local, roads_express)
        
    
    # Step 2) For each edge (pair of nodes) adding weights and then adding edge to the graph
    
    for road in all_roads:
        
        ## Step 2.1) Collecting information on the nodes
        
        node1, node2 = road[0], road[1]
                
        x1, y1 = node1[0], node1[1]
        x2, y2 = node2[0], node2[1]
        
        # Determining the road type
        
        # It is a local road
        if member(road, roads_local):
            road_type = 'LR'
            road_type_cost = cost_km_LR
            
        # It is an express road
        else:
            road_type = 'ER'
            road_type_cost = cost_km_ER

        
        ## Step 2.2) Calculating the road_weight
        # Edge weight = euclidean distance * cost_road_type

        # Calculating euclidean distance
        eucl_dist = np.sqrt((x2 - x1)^2 + (y2 - y1)^2)
        
        # Multiplying with cost of the corresponding road type
        
        road_weight = eucl_dist * road_type_cost
        
        # Step 3) Adding each edge to the graph
        Graph_all_roads = Graph_all_roads.add_weighted_edges_from([node1, node2, road_weight, road_type])
    
    return Graph_all_roads