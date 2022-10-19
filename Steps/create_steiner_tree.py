def create_steiner_tree_roads(selected_mall, set_houses, set_malls, city_center):
    
    # Setting up the terminal and non terminal nodes
    all_nodes = union(selected_mall, set_houses, set_mall, city_center)
    terminal_nodes = union(set_houses, selected_mall)

    # Creating all graphs
    Graph_all_roads = nx.Graph()
    Graph_MC_terminal = nx.Graph()
    Graph_MST_terminal= nx.Graph()
    Graph_steiner_tree = nx.Graph()

    # Step 0) Create a graph with all possible roads
    Graph_all_roads = create_graph_with_roads(set_houses, set_malls, set_city_center)
    
    # Step 1) Create MC of the terminal roads
    Graph_MC_terminal = create_graph_MC(Graph_all_roads)

    # Step 2) Create MST of terminal
    Graph_MST_terminal = create_MST(Graph_MC_terminal)

    # Step 3) Remove edges

    return steiner_tree