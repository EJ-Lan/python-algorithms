
def make_set(parent, node):
    parent[node] = node
    global rank
    rank[node] = 0

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, x, y):
    global rank
    x_rep = find(parent, x)
    y_rep = find(parent, y)
    if x_rep != y_rep:
        if rank[x_rep] > rank[y_rep]:
            parent[y_rep] = x_rep
        else:
            parent[x_rep] = y_rep
            if rank[x_rep] == rank[y_rep]:
                rank[y_rep] += 1

def print_rank(graph, parent):
    global rank
    print (rank)

# below here is specific for graphs

def initialize_union_find_for_graph(graph):
    parent = {}
    global rank
    rank = {}
    for node in graph:
        make_set(parent, node)
    return parent