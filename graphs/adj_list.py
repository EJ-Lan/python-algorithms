def name(node): return node[1]

def adj_list(node): return node[0]

def print_names(graph):
    print('Nodes in graph:', end = ' ')
    for node in graph:
        print(name(node), end = ' ')
    print()

def print_neighbors(graph, adj_list):
    for index in adj_list:
        print(name(graph[index]), end = ' ') 

def print_all_neighbors(graph):
    for index in range(len(graph)):
        print(f'Neighbors of node {index} = {name(graph[index])} :',
              end = ' ')
        print_neighbors(graph, adj_list(graph[index]))
        print()

def print_degrees(graph):
    for node in graph:
        print(f'Node {name(node)} has degree {len(adj_list(node))}')

##############################################################################
# test:

def test_adj_list():
    # Indices of nodes:
    # BC = node 0
    # AB = node 1
    # SK = node 2
    # MT = node 3
    western_canada = [ ([1]  , 'BC'), # [1] = List of neighbors of BC
                       ([0,2], 'AB'), # List of neighbors of AB
                       ([1,3], 'SK'), # List of neighbors of SK
                       ([2]  , 'MT')  # List of neighbors of MT
                     ]

    print_names(western_canada)
    print_all_neighbors(western_canada)
    print_degrees(western_canada)

if __name__ == '__main__':
    test_adj_list()