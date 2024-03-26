from collections import deque

INFINITY = float('inf')

def bfs(graph, distance, queue, do_print = False):
    while len(queue) > 0:
        node = queue.popleft();
        if do_print: print(f'node {node} at distance {distance[node]}')
        #print(f'{node} {distance[node]}')
        d = distance[node] + 1 # neighbors are 1 further away
        for neighbor in graph[node]:
            if distance[neighbor] == INFINITY:
                if do_print: print(f'{neighbor} is new neighbor of {node}')
                queue.append(neighbor)
                distance[neighbor] = d

def breadth_first_search(graph, start, do_print = False):
    distance = {node: INFINITY for node in graph}
    if do_print: print(f'\nstarting bfs from {start}')
    queue = deque()
    queue.append(start)
    distance[start] = 0
    bfs(graph, distance, queue, do_print)
    return distance

##############################################################################
# test:
from undirected_graph_examples import slides_example, western_canada, dasgupta_book_fig3_2
from directed_graph_examples import bookfigure3point7

def run_bfs_from_all_start_nodes(graph, name):
    print("\nRunning bfs from all possible starting points for", name)
    for node in graph:
        breadth_first_search(graph, node, do_print = True)

def test_bfs():
    print('slides example')
    breadth_first_search(slides_example, 2)
    run_bfs_from_all_start_nodes(western_canada, "Western Canada")
    run_bfs_from_all_start_nodes(dasgupta_book_fig3_2, 
                                 "Dasgupta book Figure 3.2")
    run_bfs_from_all_start_nodes(bookfigure3point7, "Book Figure 3.7")

if __name__ == '__main__':
    test_bfs()