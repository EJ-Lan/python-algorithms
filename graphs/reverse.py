def reverse(graph):
    r_graph = {node: [] for node in graph} # init. with empty adj. lists
    for node in graph:
        for neighbor in graph[node]:
            r_graph[neighbor].append(node)
    return r_graph