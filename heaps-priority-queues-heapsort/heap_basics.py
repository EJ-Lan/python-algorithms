import math

def parent(index):
    return index // 2

def left_child(index):
    return 2 * index

def right_child(index):
    return 2 * index + 1

def heap_size(heap):
    return len(heap) - 1

def height(heap):
    n = heap_size(heap)
    return math.floor(math.log(n, 2))

def check_heap_property(heap, has_heap_property, start):
    n = heap_size(heap)
    for i in range(start, n//2 + 1):
        if not has_heap_property(heap, i):
            return False
    return True

def is_heap(heap, has_heap_property, start=1):
    return check_heap_property(heap, has_heap_property, start)

def is_almost_heap(heap, has_heap_property, start=1):
    return check_heap_property(heap, has_heap_property, start + 1)

def print_tree(heap, index = 1, level = 0):
    if index <= heap_size(heap):
        print_tree(heap, right_child(index), level + 1)
        if level == 0: print(heap[index])
        else: print(' ' * 3 * level, heap[index])
        print_tree(heap, left_child(index), level + 1)