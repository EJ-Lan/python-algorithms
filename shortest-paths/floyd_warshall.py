from edge_with_length import other_end, length

INFINITY = float('inf')

# nodes in graph are numbered 1,2,... in their dictionary traversal order.
# Then weights matrix is constructed using these indices
def weight_matrix(graph):
    n = len(graph)
    index = {}
    next = 1
    for node in graph:
        index[node] = next
        next += 1
    w = [[INFINITY for _ in range(n+1)] for _ in range(n+1)]
    for node in graph:
        i = index[node]
        w[i][i] = 0
        for edge in graph[node]:
            j = index[other_end(edge)]
            w[i][j] = length(edge)
    return w

def print_path(i, j, b):
    mid = b[i][j]
    if mid == 0: 
        print(f'{i}-{j}', end = ' ')
    else:
        print_path(i, mid, b)
        print_path(mid, j, b)

def print_paths(b, n):
    print('All shortest paths:')
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(f'From {i} to {j}:', end = ' ')
            print_path(i, j, b)
            print()

def print_d(d, n):
    print('d')
    for k in range(n+1):
        print(f'k = {k}')
        for i in range(1, n+1):
            for j in range(1, n+1):
                print(f'{d[i][j][k]:4}', end = ' ')
            print()
        print()
    print()

def print_b(b, n):
    print('b')
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(b[i][j], end = ' ')
        print()
    print()

def floyd_warshall(graph):
    n = len(graph)
    w = weight_matrix(graph)
    print_b(w, n)
    # not using index 0 to be compatible with pseudocode in slides
    d = [[[INFINITY for k in range(n+1)] for j in range(n+1)] for i in range(n+1)]
    b = [[0 for j in range(n+1)] for i in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j][0] = w[i][j]
    #print_d(d, n)
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if d[i][k][k - 1] + d[k][j][k - 1] < d[i][j][k - 1]:
                # new shorter path through k
                    d[i][j][k] = d[i][k][k - 1] + d[k][j][k - 1]
                    b[i][j] = k
                else: # best path is the old one without k
                    d[i][j][k] = d[i][j][k - 1]
    print_d(d, n)
    print_b(b, n)
    print_paths(b, n)
    return d, b

##############################################################################
# test:
import sample_graphs_with_lengths as graphs

def test_floyd_warshall():
    floyd_warshall(graphs.floyd_warshall_example)
    
if __name__ == '__main__':
    test_floyd_warshall()
