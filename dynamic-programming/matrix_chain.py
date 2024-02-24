INFINITY = float('inf')

def multiply(d, do_print = False):
    n = len(d) - 1 # d has n+1 elements d[0]..d[n]
    M = [[0 for j in range(n+1)] for i in range(n+1)]
    S = [[None for j in range(n+1)] for i in range(n+1)]
    
    for gap in range(1,n):
        for i in range(1, n - gap + 1):
            M[i][i+gap] = INFINITY
            for k in range(gap):
                cut_at_k = M[i][i+k] + M[i+k+1][i+gap] \
                         + d[i-1] * d[i+k] * d[i+gap]
                if cut_at_k < M[i][i+gap]:
                    M[i][i+gap] = cut_at_k
                    S[i][i+gap] = i+k
    if do_print:
        #print(M)
        #print(S)
        print_opt_order(S, 1, n, outermost = True)
    return M[1][n]

# print optimal multiplication order with correct bracketing
# The pseudocode in slides brackets everything
# The code here does not bracket single matrices, or the whole expression.
# It is a more human style bracketing
def print_opt_order(S, i, j, outermost = False):
    if i == j:
        print(f'A{i}', end = '')
    else:
        if not outermost: print('(', end = '')
        print_opt_order(S, i, S[i][j])
        print('*', end = '')
        print_opt_order(S, S[i][j] + 1, j)
        if not outermost: print(')', end = '')
    if outermost: print()

def test_matrix_chain():
    print("Two matrices")
    num = multiply([1,3,2], do_print = True)
    assert num == 6
    print(num)

    print("Example 1 from slides")
    num = multiply([5,2,6,4,3], do_print = True)
    assert num == 102
    print(num)

    print("Example 2 from slides")
    num = multiply([5,4,6,2,7], do_print = True)
    assert num == 158
    print(num)
    
    print('Random larger example')
    num = multiply([5,4,10,6,2,7,15,17,23], do_print = True)
    print(num)

    print('Random larger example')
    num = multiply([12,11,7,6,5,4,3,2,1,10,9,8,1,2,3,7,8,9,4,5,6,10,11], do_print = True)
    print(num)

if __name__ == '__main__':
    test_matrix_chain()