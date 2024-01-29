import random
import time
import test_random_lists

def is_sorted(sequence):
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence) - 1))

# Merge two sequences and return the result in a new list
def merge2(b, c):
    result = list()
    b_head = 0
    c_head = 0
    b_length = len(b)
    c_length = len(c)
    while b_head < b_length and c_head < c_length: # both non-empty
        if b[b_head] < c[c_head]:
            result.append(b[b_head])
            b_head += 1
        else:
            result.append(c[c_head])
            c_head += 1
    # now one of b, c is empty. Copy the rest of the other input.
    while b_head < b_length:
        result.append(b[b_head])
        b_head += 1
    while c_head < c_length:
        result.append(c[c_head])
        c_head += 1
    assert len(result) == b_length + c_length
    assert is_sorted(result)
    return result

# Note this code is a bit different from the pseudo code.
# It creates the merged results in a new space.
# The pseudo code cannot be implemented directly as written (in-place).
def merge_sort(a,low,high):
    if low < high:
        mid = (low + high) // 2
        result1 = merge_sort(a, low, mid)
        result2 = merge_sort(a, mid+1, high)
        result = merge2(result1, result2)
        return result
    else: # base case, single number, nothing to sort
        assert low == high
        return [a[low]] # list with one number in it

def run_merge_sort(a):
    result = merge_sort(a, 0, len(a) - 1)
    assert len(result) == len(a)
    assert is_sorted(result)
    return result

# test:
def test_merge2(b, c):
    print(f'Test merge: b = {b}, c = {c}, result = {merge2(b, c)}')

def test_merge_sort(a):
    print(f'Test merge sort: {a}')
    a = run_merge_sort(a)
    print(f'Result: {a}')

def test_all_merge_sort():
    print(f'Test merge sort')
    test_merge2([1, 3, 5, 7], [2, 4, 6, 8])
    test_merge2([1, 3, 5, 7], [])
    test_merge2([], [2, 4, 6, 8])
    test_merge2([1, 10, 100, 1000], [2, 4, 6, 8])
    test_merge_sort([1, 3, 5, 7, 2, 4, 6, 8, 10])
    test_random_lists.test_random_lists(run_merge_sort, num_doublings = 20)

if __name__ == '__main__':
    test_all_merge_sort()