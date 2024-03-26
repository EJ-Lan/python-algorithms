from reverse import reverse

WHITE = 0
GREY  = 1
BLACK = 2

INFINITY = float('inf')

class Data:
    def __init__(self):
        self.color = WHITE
        self.predec = None # predecessor in dfs tree

# A sink has no outgoing edges.
def sink_nodes(graph):
    sinks = []
    for node in graph:
        if len(graph[node]) == 0: # no neighbors in adj list
            sinks.append(node)
    return sinks
    
# A source has no incoming edges. It is a sink in the reverse graph
def source_nodes(graph):
    return sink_nodes(reverse(graph))
    
def print_list(nodes):
    for node in nodes:
        print(node, end = ' ')
    print()
    
# We detected a cycle connecting last_node back to first_node.
# We find all nodes in reverse order by following predec 
# in dfs back to first_node
def print_cycle(graph_data, first_node, last_node):
    cycle = [first_node]
    node = last_node
    cycle.append(node)
    while node != first_node:
        node = graph_data[node].predec
        assert node != None
        cycle.append(node)
    print(f'Cycle detected:', end = ' ')
    for node in reversed(cycle):
        print(node, end = ' ')
    print()

# returns True if cycle found
def dfs_visit(graph, graph_data, node, depth):
    print('  ' * depth, f'Start  dfs_visit node {node}')
    graph_data[node].color = GREY
    for neighbor in graph[node]:
        if graph_data[neighbor].color == WHITE:
            graph_data[neighbor].predec = node
            if dfs_visit(graph, graph_data, neighbor, depth+1):
                return True
        elif graph_data[neighbor].color == GREY:
            print_cycle(graph_data, neighbor, node)
            return True
    graph_data[node].color = BLACK
    return False

def dfs_find_cycle(graph):
    graph_data = {}
    for node in graph:
        graph_data[node] = Data()
    has_cycle = False
    for node in graph:
        if graph_data[node].color == WHITE:
            if dfs_visit(graph, graph_data, node, 0): # cycle, stop
                has_cycle = True
                break
    if not has_cycle: print('No cycle, graph is a DAG')

##############################################################################
# test:
from undirected_graph_examples import slides_example, slides_example_reordered, western_canada, dasgupta_book_fig3_2
from directed_graph_examples import simple, lecture29_slide29, lecture29_slide29b, lecture29_slide30, lecture29_slide32_cycle, bookfigure3point7

def test_graph(graph):
    dfs_find_cycle(graph)
    print('Source nodes:', end = ' ')
    print_list(source_nodes(graph))
    print('Sink nodes:', end = ' ')
    print_list(sink_nodes(graph))

def test_dfs_find_cycle():
    print("dfs for directed_graph simple")
    test_graph(simple)
    print("dfs for directed_graph lecture29_slide29")
    test_graph(lecture29_slide29)
    print("dfs for directed_graph lecture29_slide29b")
    test_graph(lecture29_slide29b)
    print("dfs for directed_graph lecture29_slide30")
    test_graph(lecture29_slide30)
    print("dfs for directed_graph lecture29_slide32_cycle")
    test_graph(lecture29_slide32_cycle)
    
    
    print("dfs for undirected_graph slides_example")
    test_graph(slides_example)
    print("dfs for undirected_graph slides_example_reordered")
    test_graph(slides_example_reordered)
    
    print("dfs for undirected_graph western_canada")
    test_graph(western_canada)
#     print("\ndfs for dasgupta_book_fig3_2")
#     dfs(dasgupta_book_fig3_2)
#     print("\ndfs for bookfigure3point7")
#     dfs(bookfigure3point7)

if __name__ == '__main__':
    test_dfs_find_cycle()