from is_sorted import is_sorted
from random_list import random_list

def insertion_sort_trace(a):
    n = len(a)
    print(f'Original sequence: {a}')
    for j in range(1, n): 
        print('-'*40)
        print(f'j = {j}')
        print(f'Insert key a[j] = a[{j}] = {a[j]} into sorted sublist a[0..{j-1}] = {a[0:j]}')
        key = a[j]
        i = j - 1
        print(f'Move up elements in a[0..{j-1}] that are larger than the key')
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            print(f'    Shift a[{i}] to a[{i + 1}]: sublist now: {a[0:j+1]}')
            i = i - 1
        if i == j-1:
            print(f'    Nothing to move')
        a[i + 1] = key
        print(f'Add key {key} in a[{i + 1}]: new sorted sublist a[0..{j}] = {a[0:j+1]}')
    print(f'Final sorted sequence: {a}')
    
if __name__ == '__main__':
    numbers = [53, 21, 47, 62, 14, 38]
    insertion_sort_trace(numbers)