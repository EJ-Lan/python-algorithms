def dfs_visit(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_visit(graph, neighbor, visited, stack)
    stack.append(node)

def dfs_ftime_stack(graph):
    stack = []
    visited = {}
    for node in graph:
        visited[node] = False
    for node in graph:
        if not visited[node]:
            dfs_visit(graph, node, visited, stack)
    return stack