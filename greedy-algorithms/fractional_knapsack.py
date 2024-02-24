import quick_sort

class Item:
    def __init__(self, w, b, name = ''):
        assert w > 0
        assert b > 0
        self.w = w
        self.b = b
        self.name = name
        
    # the >= operator for Item. Sorts by value. 
    # Operator is needed for key comparison in the 
    # quicksort partition function
    def __ge__(self, other): 
       return self.value() >= other.value()

    def __str__(self):
        return f'({self.name} w = {self.w}, b = {self.b}, v = {self.value()})'
        
    def value(self):
        return self.b / self.w

def print_items(S):
    for i in range(len(S)):
        print(S[i])

def print_solution(S, x):
    print(f'\nGreedy solution:')
    assert len(S) == len(x)
    for i in range(len(S)):
        if x[i] > 0:
            print(f'{x[i]} of {S[i].name}')

def fractional_knapsack(W, S):
    print_items(S[1:])
    quick_sort.call_quick_sort(S)
    S = S[1:] # get rid of the None in S[0]
    n = len(S)
    print('\nAfter sorting:')
    print_items(S)
    x = [0 for _ in range(n)]
    currentW = 0
    i = n - 1 # sorted in increasing order, so best v are at the end
    while currentW < W and i >= 0:
        x[i] = min(S[i].w, W - currentW)
        currentW += x[i]
        i -= 1
    print_solution(S, x)

def test_fractional_knapsack():
    print('Example from slides')
    S = [None, # for 1-based quicksort
        Item(2, 6, 'Cumin'),
        Item(2, 8, 'Saffron'),
        Item(5, 10, 'Pepper'),
        Item(1.5, 4, 'Nutmeg'),
        Item(1, 3, 'Turmeric'),
        Item(3, 9, 'Paprika')]
    fractional_knapsack(4, S)

    print('\nExample from slides but with larger knapsack')
    S = [None, # for 1-based quicksort
        Item(2, 6, 'Cumin'),
        Item(2, 8, 'Saffron'),
        Item(5, 10, 'Pepper'),
        Item(1.5, 4, 'Nutmeg'),
        Item(1, 3, 'Turmeric'),
        Item(3, 9, 'Paprika')]
    fractional_knapsack(10, S)

    print('\nExample with too-big knapsack')
    S = [None, # for 1-based quicksort
        Item(2, 6, 'Cumin'),
        Item(2, 8, 'Saffron'),
        Item(5, 10, 'Pepper')]
    fractional_knapsack(40, S)

if __name__ == '__main__':
    test_fractional_knapsack()