import heapq
from edge_with_length import other_end, length

INFINITY = float('inf')

print_decrease_key = False

def dijkstra(graph, start, print_trace = False):
    distance = {node: INFINITY for node in graph}
    distance[start] = 0
    previous = {}
    previous[start] = None
    q = [(0, start)]
    # priority queue using distance-values as keys
    while len(q) > 0:
        (dist, u) = heapq.heappop(q) #delete_min
        if dist > distance[u]: # ignore old entry with too-high distance
            continue
        if print_trace:
            print(f'distance to {u} is {dist}')
        for edge in graph[u]:
            l = length(edge)
            v = other_end(edge)
            if distance[v] > distance[u] + l: # New, better path to v
                distance[v] = distance[u] + l
                previous[v] = u
                # pq.decrease_key(q, v, distance[v])
                # we leave the old entry in the queue since there is 
                # no fast way to find it
                if print_decrease_key: 
                    print ("Decreasekey for", v, "to", distance[v])
                heapq.heappush(q, (distance[v], v))
    #print ("Dijkstra from", start, ":")
    #print ("Distances:", distance)
    #print ("Previous:", previous)
    #return distance
    return (distance, previous)
    
##############################################################################
# test:

import sample_graphs_with_lengths as graphs

def print_path(start, end_point, previous):
    path = [end_point]
    while previous[end_point] is not None:
        end_point = previous[end_point]
        path.append(end_point)
    for node in reversed(path): print(node, end = ' ')
    print()

# result contains two dictionaries with shortest distances and previous
def print_result(result, start):
    distances, previous = result
    print("Shortest distances from", start)
    print(distances)
    print("Previous links", previous)
    for end_point in previous:
        print(f'Shortest path from {start} to {end_point}:')
        print_path(start, end_point, previous)
    
def test_dijkstra():
    test_cases = [ (graphs.lecture32_slide8, 'UA'),
#                    (graphs.abc, 'A'),
#                    (graphs.western_canada, 'AB'),
#                    (graphs.book, 'A'),
#                    (graphs.book, 'E'),
#                    (graphs.ryans_example, 'A'),
                   (graphs.dijkstra_bad_case, 'A')
    ]
    
    for test_case in test_cases:
        graph, start = test_case
        result = dijkstra(graph, start, print_trace = True)
        print_result(result, start)

if __name__ == '__main__':
    test_dijkstra()