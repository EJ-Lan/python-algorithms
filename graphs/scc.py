from dfs_ftime_stack import dfs_ftime_stack
from reverse import reverse

def dfs_visit(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_visit(graph, neighbor, visited, component)

def print_component(i, component):
    print (f'Component {i}:', end = ' ')
    for node in component:
        print(node, end = ' ')
    print()

def print_components(components):
    for i, component in enumerate(components):
        print_component(i+1, component)

def scc(graph):
    # First dfs
    stack = dfs_ftime_stack(graph)
    # Second dfs on reverse graph
    print(f'Processing order for second dfs:', end = ' ')
    for n in reversed(stack): print(f'{n}', end = ' ')
    print()
    rGraph = reverse(graph)
    visited = {}
    for node in rGraph:
        visited[node] = False
    components = []
    while len(stack) > 0:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_visit(rGraph, node, visited, component)
            components.append(component)
    print (f'This graph has {len(components)} strongly connected components:')
    print_components(components)

##############################################################################
# test:

from directed_graph_examples import simple, lecture30_slide18, lecture30_slide19, lecture30_slide22, bookfigure3point7, bookfigure3point8, bookfigure3point9, bookfigure3point10

def test_scc():
    print ("\nscc for simple graph:")
    scc(simple)
    
    print ("\nscc for lecture30_slide18:")
    scc(lecture30_slide18)
    
    print ("\nscc for lecture30_slide19:")
    scc(lecture30_slide19)
    
    print ("\nscc for reverse(lecture30_slide19):")
    scc(reverse(lecture30_slide19))
    
    print ("\nscc for lecture30_slide22:")
    scc(lecture30_slide22)
    
    
    
#     print ("\nscc for dasgupta textbook figure 3.7:")
#     scc(bookfigure3point7)
# 
#     print ("\nscc for dasgupta textbook figure 3.8:")
#     scc(bookfigure3point8)
# 
#     print ("\nscc for dasgupta textbook figure 3.9:")
#     scc(bookfigure3point9)
# 
#     print ("\nscc for dasgupta textbook figure 3.10:")
#     scc(bookfigure3point10)

if __name__ == '__main__':
    test_scc()
