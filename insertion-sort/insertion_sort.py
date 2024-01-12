from is_sorted import is_sorted
from random_list import random_list

def insertion_sort(a):
    n = len(a)
    for j in range(1, n): # insert a[j] into sorted sublist a[0..j-1]
        assert is_sorted(a[0:j])
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    
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

if __name__ == '__main__':
    test_insertion_sort()