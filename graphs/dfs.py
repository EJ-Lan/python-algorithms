def dfs_visit(graph, node, visited):
    visited.append(node)
    print ("dfs_visit from", node, ", visited", visited)
    for neighbor in graph[node]:
        if neighbor in visited:
            print("Skip neighbor", neighbor, "of", node, ", already visited")
        else:
            dfs_visit(graph, neighbor, visited)
    print ("done exploring from", node)

def dfs(graph):
    visited = []
    for node in graph:
        if node not in visited:
            dfs_visit(graph, node, visited)

##############################################################################
# test:
from undirected_graph_examples import slides_example, western_canada, dasgupta_book_fig3_2
from directed_graph_examples import bookfigure3point7

def test_dfs():
    print("dfs for slides_example")
    dfs(slides_example)
    print("dfs for western_canada")
    dfs(western_canada)
#     print("\ndfs for dasgupta_book_fig3_2")
#     dfs(dasgupta_book_fig3_2)
#     print("\ndfs for bookfigure3point7")
#     dfs(bookfigure3point7)

if __name__ == '__main__':
    test_dfs()
