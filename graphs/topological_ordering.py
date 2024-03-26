from dfs_ftime_stack import dfs_ftime_stack

def topological_ordering(graph):
    order = reversed(dfs_ftime_stack(graph))
    print ("Topological ordering:")
    for node in order: print(node, end = ' ')
    print()

##############################################################################
# test:
from directed_graph_examples import simple, bookfigure3point8, lecture29_slide29, lecture29_slide29b, lecture29_slide30

def test_topological_ordering():
    print("dfs for simple graph")
    topological_ordering(simple)
    print("dfs for directed_graph lecture29_slide29")
    topological_ordering(lecture29_slide29)
    print("dfs for directed_graph lecture29_slide29b")
    topological_ordering(lecture29_slide29b)
    print("dfs for directed_graph lecture29_slide30")
    topological_ordering(lecture29_slide30)
    print("dfs for bookfigure3point8")
    topological_ordering(bookfigure3point8)
   

if __name__ == '__main__':
    test_topological_ordering()
