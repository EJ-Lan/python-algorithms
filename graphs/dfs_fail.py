from undirected_graph_examples import slides_example

def dfs(graph, node):
    print ("dfs from", node)
    for neighbor in graph[node]:
        dfs(graph, neighbor)

dfs(slides_example, 1)
