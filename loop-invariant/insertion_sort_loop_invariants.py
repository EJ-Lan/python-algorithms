from is_sorted import is_sorted
from random_list import random_list


# Loop invariant: At beginning of "loop for j", A[0,..j-1] 
# are the same numbers as in the input, but in sorted order, 
# i.e. A[0] <= A[1] <= ... <= A[j-1]
def check_for_loop_invariant(a, a_start, j):
    assert is_sorted(a[0:j])
    a_numbers = set(a[0:j])
    a_start_numbers = set(a_start[0:j])
    assert a_numbers == a_start_numbers
    
# Loop invariant: at start of "iteration for i", 
# A[0..i+1] = A^before[0..i+1], and
# A[i+2..j] = A^before[i+1..j-1], and all these numbers are larger than the key
def check_while_loop_invariant(a, a_before, j, i, key):
    for k in range(i+2):
        assert a[k] == a_before[k]
    for k in range(i+2, j):
        assert a[k] == a_before[k-1]
        assert a[k] > key

def insertion_sort(a):
    n = len(a)
    a_start = a.copy()
    for j in range(1, n): # insert a[j] into sorted sublist a[0..j-1]
        check_for_loop_invariant(a, a_start, j)
        key = a[j]
        i = j - 1
        a_before = a.copy()
        while i >= 0 and a[i] > key:
            check_while_loop_invariant(a, a_before, j, i, key)
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    check_for_loop_invariant(a, a_start, n)

# tests
def test_insertion_sort_for(numbers):
    print(f'Before insertion_sort: {numbers}')
    insertion_sort(numbers)
    print(f'After insertion_sort: {numbers}')
    assert is_sorted(numbers)

def test_insertion_sort():
    test_insertion_sort_for([])
    test_insertion_sort_for([2, 1])
    numbers = [53, 21, 47, 62, 14, 38]
    test_insertion_sort_for(numbers)
    numbers = random_list(100)
    test_insertion_sort_for(numbers)
    texts = ['hello', 'world', 'an', 'unsorted', 'list']
    test_insertion_sort_for(texts)

if __name__ == '__main__':
    test_insertion_sort()
