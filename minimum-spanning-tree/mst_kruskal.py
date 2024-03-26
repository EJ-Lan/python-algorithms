import union_find as uf
from edge_with_length import other_end, length

# edge for sorting, represented as 3-element list [length, u, v]
def endpoint(edge, index):
    assert index >= 1
    assert index <= 2
    return edge[index]

# Generate list of undirected graph edges in format [length, u, v]
# which makes it easy to sort by length
# Only takes edges for which comparison u < v is true
# this avoids duplicates and loops
def extract_edges(graph):
    edges = []
    for node in graph:
        for edge in graph[node]:
            v = other_end(edge)
            if node < v:
                edges.append([length(edge), node, v])
    return edges

def sort_edges(graph):
    edges = extract_edges(graph)
    edges.sort()
    return edges

def minimum_spanning_tree(graph, trace = True):
    clusters = uf.initialize_union_find_for_graph(graph)
    mst = []
    sorted_edges = sort_edges(graph)
    for edge in sorted_edges:
        if trace: print(f'Processing edge {edge}', end = ' ')
        u = endpoint(edge, 1)
        v = endpoint(edge, 2)
        if uf.find(clusters, u) != uf.find(clusters, v):
            mst.append(edge)
            uf.union(clusters, u, v)
            print('adding edge')
        else: print('ignoring edge within same component')
    return mst

##############################################################################
# test:
import sample_graphs_with_lengths as graphs

def print_result(mst):
    print('Edges in MST:', end = ' ')
    for edge in mst:
        print(f'{edge}', end = ' ')
    print()
    
def test_minimum_spanning_tree():
    mst = minimum_spanning_tree(graphs.slides_example)
    print_result(mst)

    mst = minimum_spanning_tree(graphs.slides_example2)
    print_result(mst)

#     mst = minimum_spanning_tree(graphs.abcundirected)
#     print_result(mst)
# 
#     mst = minimum_spanning_tree(graphs.western_canada)
#     print_result(mst)
# 
#     mst = minimum_spanning_tree(graphs.bookundirected)
#     print_result(mst)
# 
#     mst = minimum_spanning_tree(graphs.ryansExample)
#     print_result(mst)

if __name__ == '__main__':
    test_minimum_spanning_tree()
