WHITE = 0
GREY  = 1
BLACK = 2

INFINITY = float('inf')

class Data:
    def __init__(self):
        self.color = WHITE
        self.predec = None # predecessor in dfs tree
        self.dtime = INFINITY # discovery time
        self.ftime = INFINITY # finish time

def dfs_visit(graph, graph_data, node, depth):
    global clock
    clock += 1
    print('  '*depth, f'Start  dfs_visit node {node} at time {clock}')
    graph_data[node].color = GREY
    graph_data[node].dtime = clock
    for neighbor in graph[node]:
        if graph_data[neighbor].color == WHITE:
            graph_data[neighbor].predec = node
            dfs_visit(graph, graph_data, neighbor, depth+1)
    graph_data[node].color = BLACK
    clock += 1
    print('  '*depth, f'Finish dfs_visit node {node} at time {clock}')
    graph_data[node].ftime = clock

def dfs(graph):
    global clock
    clock = 0
    graph_data = {}
    for node in graph:
        graph_data[node] = Data()
    for node in graph:
        if graph_data[node].color == WHITE:
            dfs_visit(graph, graph_data, node, 0)
    print ("Timestamps:")
    for node in graph:
        print(f'{node} [{graph_data[node].dtime}:{graph_data[node].ftime}]')
    print ("Predecessors in DFS tree:")
    for node in graph:
        print(f'{node} [{graph_data[node].predec}]')

##############################################################################
# test:
from undirected_graph_examples import slides_example, slides_example_reordered, western_canada, dasgupta_book_fig3_2
from directed_graph_examples import bookfigure3point7

def test_dfs():
    print("dfs for slides_example")
    dfs(slides_example)
    print("dfs for slides_example_reordered")
    dfs(slides_example_reordered)
    
    print("dfs for western_canada")
    dfs(western_canada)
#     print("\ndfs for dasgupta_book_fig3_2")
#     dfs(dasgupta_book_fig3_2)
#     print("\ndfs for bookfigure3point7")
#     dfs(bookfigure3point7)

if __name__ == '__main__':
    test_dfs()