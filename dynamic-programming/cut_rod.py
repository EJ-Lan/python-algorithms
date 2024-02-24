INFINITY = float('inf')

def print_result(r, best):
    total = 0
    assert len(r) == len(best)
    n = len(r) - 1
    print(f'Best value {r[n]}:')
    print(f'Cut rod of length {n} into pieces of length:', end = ' ')
    if best[n] == None: 
        print(n)
    else:
        remaining = n
        while best[remaining] != None:
            print(best[remaining], end = ' ')
            remaining -= best[remaining]
        print()
        

def cut_rod(p, n, do_print = False):
    assert len(p) == n + 1 # We use p[1] .. p[n]
    assert p[0] == None
    r = [0 for _ in range(n+1)]
    best = [None for _ in range(n+1)]
    for j in range(1, n + 1):
        q = -INFINITY
        for i in range(1, j + 1):
            v = p[i] + r[j-i]
            if v > q:
                q = v
                best_i = i
        r[j] = q
        best[j] = best_i
    if do_print: 
        print('p=', p)
        print('r=', r)
        print('best=', best)
        print_result(r, best)
    return r[n]

def test_cut_rod():
    print('First example from slides')
    p = [None, 2, 6, 7, 11, 13]
    value = cut_rod(p, len(p)-1, True)
    assert value == 14
    
    # https://sites.radford.edu/~nokie/classes/360/dp-rod-cutting.html
    print('\nLength 4 example from internet')
    p = [None, 1, 5, 8, 9]
    value = cut_rod(p, len(p)-1, True)
    assert value == 10

    print('\nLength 8 example from internet')
    p = [None, 1, 5, 8, 9, 10, 17, 17, 20]
    value = cut_rod(p, len(p)-1, True)
    assert value == 22

    print('\nExample where not cutting is best')
    p = [None, 1, 5, 8, 9, 10, 17, 17, 30]
    value = cut_rod(p, len(p)-1, True)
    assert value == 30

if __name__ == '__main__':
    test_cut_rod()