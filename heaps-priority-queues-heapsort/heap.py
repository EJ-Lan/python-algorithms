from is_sorted import is_sorted
import test_random_lists
from heap_basics import parent, left_child, right_child, heap_size, height, \
check_heap_property, is_heap, is_almost_heap, print_tree

# is element at index greater-or-equal to all its children?
def has_max_heap_property(heap, index):
    size = heap_size(heap)
    assert index >= 1
    assert index <= size
    lc = left_child(index)
    rc = right_child(index)
    if lc <= size and not (heap[index] >= heap[lc]):
        return False
    if rc <= size and not (heap[index] >= heap[rc]):
        return False
    return True

    
def max_heapify(heap, i, size):
    # assert here is too slow, Theta(n), kills runtime. 
    # assert is_almost_heap(heap, i)
    assert i >= 1
    assert i <= size
    lc = left_child(i)
    rc = right_child(i)
    largest = i
    if lc <= size and not (heap[largest] >= heap[lc]):
        largest = lc
    if rc <= size and not (heap[largest] >= heap[rc]):
        largest = rc
    if largest != i: # largest is a child, needs swap and recursion
        temp = heap[i]
        heap[i] = heap[largest]
        heap[largest] = temp
        max_heapify(heap, largest, size)
    # Checking the whole heap here is too slow, Theta(n), kills runtime. 
    # assert is_heap(heap, i)
    
def build_max_heap(heap):
    assert heap[0] == None
    size = heap_size(heap)
    for i in range(size//2, 0, -1):
        max_heapify(heap, i, size)
    assert is_heap(heap, has_max_heap_property, 1)
  
# Needed for priority queue. Not needed for heapsort.
def increase_key(heap, index, key):
    assert index >= 1
    assert index <= heap_size(heap)
    assert key >= heap[index]
    heap[index] = key
    p = parent(index)
    while index > 1 and heap[p] < heap[index]:
        # trickle up
        temp = heap[p]
        heap[p] = heap[index]
        heap[index] = temp
        index = p
        p = parent(index)
    assert is_heap(heap, has_max_heap_property)
 
# Needed for priority queue. Not needed for heapsort.
def insert(heap, key):
    heap.append(key)
    increase_key(heap, heap_size(heap), key)

##############################################################################
# test:
def test_heap():
    a = [None, 1, 3, 5, 7, 2, 4, 6, 8, 10]
    print(f'a = {a[1:]}')
    print_tree(a)
    build_max_heap(a)
    print(f'after build_max_heap, a = {a[1:]}')
    print_tree(a)
    test_random_lists.test_random_one_based_lists(build_max_heap)

if __name__ == '__main__':
    test_heap()