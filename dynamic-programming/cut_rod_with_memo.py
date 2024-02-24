INFINITY = float('inf')

def cut_rod(p, n):
    assert len(p) == n + 1 # We use p[1] .. p[n]
    assert p[0] == None
    memo = dict()
    return cut_rod_memo(p, n, memo)

def cut_rod_memo(p, n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    q = -INFINITY
    for i in range(1, n + 1):
        v = p[i] + cut_rod_memo(p, n-i, memo)
        if v > q:
            q = v
    memo[n] = q
    return q

def test_cut_rod():
    print('First example from slides')
    p = [None, 2, 6, 7, 11, 13]
    value = cut_rod(p, len(p)-1)
    print(value)
    assert value == 14
    
    # https://sites.radford.edu/~nokie/classes/360/dp-rod-cutting.html
    print('\nLength 4 example from internet')
    p = [None, 1, 5, 8, 9]
    value = cut_rod(p, len(p)-1)
    print(value)
    assert value == 10

    print('\nLength 8 example from internet')
    p = [None, 1, 5, 8, 9, 10, 17, 17, 20]
    value = cut_rod(p, len(p)-1)
    print(value)
    assert value == 22

    print('\nExample where not cutting is best')
    p = [None, 1, 5, 8, 9, 10, 17, 17, 30]
    value = cut_rod(p, len(p)-1)
    print(value)
    assert value == 30

if __name__ == '__main__':
    test_cut_rod()