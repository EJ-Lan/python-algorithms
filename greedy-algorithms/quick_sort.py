import test_random_lists
from is_sorted import is_sorted

# check that the partition function worked correctly
def check_partition(a, first, last, pivot_index, pivot_value, compare):
    assert a[pivot_index] == pivot_value
    for i in range(first, pivot_index):
        assert compare(a[i], pivot_value)
    for i in range(pivot_index + 1, last + 1):
        assert compare(pivot_value, a[i])

def less_equal(item1, item2):
    return item1 <= item2

def greater_equal(item1, item2):
    return item1 >= item2

# pick a pivot and then partition a[first..last]
# returns the index of the pivot
def partition(a, first, last, compare):
    assert last > first
    pivot = a[last]
    i = first - 1
    for j in range(first, last):
        if compare(a[j], pivot):
            i += 1
            a[i], a[j] = a[j], a[i] # swap. This works in Python
    a[i+1], a[last] = a[last], a[i+1] # swap pivot into right place
    check_partition(a, first, last, i+1, pivot, compare)
    return i + 1


def quick_sort(a, first, last, compare = less_equal, print_trace = False):
    assert first >= 1
    assert last <= len(a) - 1
    assert a[0] == None # Ignore a[0]; 1-based as in slides and CLRS
    
    if first < last:
        q = partition(a, first, last, compare)
        if print_trace:
            print(f'qsort {first}..{last} q = {q}')
        quick_sort(a, first, q - 1, compare, print_trace)
        quick_sort(a, q + 1, last, compare, print_trace)
    else:
        if print_trace:
            print(f'qsort {first}..{last} at most one number')

def call_quick_sort(a, compare = less_equal):
    quick_sort(a, 1, len(a) - 1, compare)
    assert is_sorted(a[1:], compare)

  ##############################################################################
# test:

def test_quick_sort(a, compare = less_equal):
    print(f'Test quicksort: {a[1:]}')
    call_quick_sort(a, compare)
    print(f'Result: {a[1:]}')

def test_all_quick_sort():
    a = [None, 1, 3, 5, 7, 2, 4, 6, 8, 10]
    test_quick_sort(a)
    a = [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_quick_sort(a)
    a = [None, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    test_quick_sort(a)
    a = [None, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    test_quick_sort(a, greater_equal)
    
    test_random_lists.test_random_one_based_lists(call_quick_sort, num_doublings = 15)

if __name__ == '__main__':
    test_all_quick_sort()