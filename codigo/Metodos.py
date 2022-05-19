import re
import sys

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    # We'll use this dict to ave the cost of visiting each node and update it as we move along the graph
    shortest_path = {}
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    # Add the start node manually
    path.append(start_node)
    
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))
    


def conversion(nodes: list):
    for j in range(len(nodes)):
        nodes[j] = re.sub("\'","",nodes[j])
    nodes[j] = nodes[j].replace('[', '(')
    nodes[j] = nodes[j].replace(']', ')')
    
    return nodes

def elementosFaltantes(init_graph):
    init_graph['(-75.5548748, 6.2517683)'] = {}
    init_graph['(-75.5809016, 6.1951511)'] = {}
    init_graph['(-75.5577674, 6.3107883)'] = {}
    init_graph['(-75.5580641, 6.3120479)'] = {}
    init_graph['(-75.5565738, 6.309374)'] = {}
    init_graph['(-75.5577593, 6.3099711)'] = {}
    init_graph['(-75.62941, 6.2708561)'] = {}
    init_graph['(-75.6371423, 6.277455)'] = {}
    init_graph['(-75.5930615, 6.1930342)'] = {}
    init_graph['(-75.5867399, 6.2402177)'] = {}
    init_graph['(-75.586747, 6.2414241)'] = {}
    
    return init_graph

def asignacion(listaO, listaD, listaL, init_graph):
    for i in range(len(listaO)):
        init_graph[listaO[i]][listaD[i]] = listaL[i]
    return init_graph

def conversion2(path):
    path = "[" + path
    path =  path + "]"
    path = path.replace('->', ' ')
    path = path.replace('(', '[')
    path = path.replace(')', ']')
    path = path.replace('  ', ', ')
    
    return path