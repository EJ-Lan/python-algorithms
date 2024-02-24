class Item:
    def __init__(self, w, v, name):
        assert w > 0
        assert v > 0
        self.w = w
        self.v = v
        self.name = name

    def __str__(self):
        return f'({self.name} w = {self.w}, v = {self.v})'
        
def get_item(items, i):
    return items[i-1]

def get_weight(items, i):
    return get_item(items, i).w

def get_value(items, i):
    return get_item(items, i).v

def printK(K, W, n):
    for item in range(n+1):
        print(f'Up to last item {item}:', end = ' ')
        for w in range(W + 1):
            print(f'{K[w][item]:3}', end = ' ')
        print()

def print_optimal_knapsack(items, K, item, D):
    if item > 0 and D > 0:
        if K[D][item] == K[D][item-1]:
            print_optimal_knapsack(items, K, item - 1, D)
        else:
            print_optimal_knapsack(items, K, item - 1, 
                                   D - get_weight(items, item))
            print(get_item(items, item))

def knapsack(W, items, do_print = False):
    n = len(items)
    # Need to initialize all K(0, j) = 0 and all K(w, 0) = 0
    # Here I just initialized the whole 2-d table to all 0
    # This also makes sure K has the dimensions (n+1),(W+1) needed
    K = [[0 for j in range(n+1)] for i in range(W+1)]
    for j in range(1, n+1):
        wj = get_weight(items, j)
        #if do_print: print (f'j = {j} wj = {wj}')
        for w in range(1, W + 1):
            withoutItemJ = K[w][j-1]
            #if do_print: print (f'w = {w}, without wj = {withoutItemJ}')
            if wj > w: # cannot choose item j
                K[w][j] = withoutItemJ
            else:
                withItemJ = get_value(items, j) + K[w - wj][j-1]
                #if do_print: print (f'w = {w}, with wj = {withItemJ}')
                K[w][j] = max(withoutItemJ, withItemJ)
    if do_print:
        printK(K, W, n)
        print('Items selected:')
        print_optimal_knapsack(items, K, n, W)
    return K[W][n]

def test_integral_knapsack():
    print('First example from slides')
    items = [
        Item(3, 10, 'Printer'),
        Item(3, 11, 'Computer'),
        Item(3, 12, 'Projector')]
    print(f'Optimum = {knapsack(6, items, do_print = True)}')

    print('Example from Lecture 24 slides 19-28')
    items = [
        Item(4, 6, 'Printer'),
        Item(2, 5, 'Computer'),
        Item(2, 4, 'Projector')]
    print(f'Optimum = {knapsack(5, items, do_print = True)}')

# http://artemisa.unicauca.edu.co/~johnyortega/instances_01_KP/
# Note the data file is in order v w, while we use w, v.
    if(False):
        print('Example f1_l-d_kp_10_269 from website')
        items = [
                Item(269, 10, 'a'),
                Item(95, 55, 'b'),
                Item(4, 10, 'c'),
                Item(60, 47, 'd'),
                Item(32, 5, 'e'),
                Item(23, 4, 'f'),
                Item(72, 50, 'g'),
                Item(80, 8, 'h'),
                Item(62, 61, 'i'),
                Item(65, 85, 'j'),
                Item(46, 87, 'k')]
        opt = knapsack(269, items, do_print = True)
        assert opt == 295
        print(f'Optimum = {opt}')

if __name__ == '__main__':
    test_integral_knapsack()