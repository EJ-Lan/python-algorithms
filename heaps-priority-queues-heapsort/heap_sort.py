import heap
import test_random_lists
from is_sorted import is_sorted

def heap_sort(a):
    assert a[0] == None # Our code is 1-based like CLRS and slides
    heap.build_max_heap(a)
    size = heap.heap_size(a)
    for i in range(size, 1, -1): # 1 not included in range. last element is 2 as in pseudocode
        temp = a[i]
        a[i] = a[1]
        a[1] = temp
        size -= 1
        heap.max_heapify(a, 1, size)
    assert is_sorted(a[1:])
  ##############################################################################
# test:

def test_heap_sort(a):
    print(f'Test heap sort: {a[1:]}')
    heap_sort(a)
    print(f'Result: {a[1:]}')
    heap.print_tree(a)

if __name__ == '__main__':
    a = [None, 1, 3, 5, 7, 2, 4, 6, 8, 10]
    test_heap_sort(a)
    a = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_heap_sort(a)
    a = [None, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    test_heap_sort(a)
    test_random_lists.test_random_one_based_lists(heap_sort)