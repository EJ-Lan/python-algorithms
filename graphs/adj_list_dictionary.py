def print_names(graph):
    print('Nodes in graph:', end = ' ')
    for node in graph:
        print(node, end = ' ')
    print()

def print_neighbors(node, graph):
    for neighbor in graph[node]:
        print(neighbor, end = ' ')
    print()

def print_all_neighbors(graph):
    for node in graph:
        print(f'Neighbors of node {node}:', end = ' ')
        print_neighbors(node, graph)

def print_degrees(graph):
    print('Node degrees:')
    for node in graph:
        print(f'Node {node} has degree {len(graph[node])}')


##############################################################################
# test:

def test_adj_list():
    western_canada = { 'BC': ['AB'],
                       'AB': ['BC', 'SK'],
                       'SK': ['AB', 'MB'],
                       'MB': ['SK']
                     }
    print_names(western_canada)
    print_all_neighbors(western_canada)
    print_degrees(western_canada)

if __name__ == '__main__':
    test_adj_list()