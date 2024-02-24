import random

def get_item(seq, i): # subtract 1 for zero-based Python sequence
    return seq[i-1]
    
def print_lcs(D, i, j, x, y):
    if i > 0 and j > 0:
        if D[i][j] == D[i-1][j]:
            sol = print_lcs(D, i-1, j, x, y)
        elif D[i][j] == D[i][j-1]:
            sol = print_lcs(D, i, j-1, x, y)
        else:
            assert D[i][j] == 1 + D[i-1][j-1]
            sol = print_lcs(D, i-1, j-1, x, y)
            assert get_item(x, i) == get_item(y, j)
            sol += get_item(x, i)
        return sol
    else: return ''

def print_table(D):
    for row in D:
        for item in row:
            print(item, end = ' ')
        print()

def get_solution(D, x, y):
    n = len(x)
    m = len(y)
    assert len(D) == n+1
    assert len(D[0]) == m+1
    return print_lcs(D, n, m, x, y)

def lcs(x, y, do_print = False, print_dp_table = False):
    n = len(x)
    m = len(y)
    D = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            D[i][j] = D[i-1][j]
            if D[i][j-1] > D[i][j]:
                D[i][j] = D[i][j-1]
            if get_item(x, i) == get_item(y, j) and \
               D[i-1][j-1] + 1 > D[i][j]:
                D[i][j] = D[i-1][j-1] + 1
    solution = get_solution(D, x, y)
    if do_print:
        print(f'LCS of {x} and {y} is length {D[n][m]}: {solution}')
    if print_dp_table: print_table(D)
    return D[n][m], solution

def random_dna(n):
    bases = 'acgt'
    dna = ''
    for _ in range(n):
        dna += random.choice(bases)
    return dna
    
def test_lcs():
    common, seq = lcs('agcctngatc', 'gagccgattc', do_print = True)
    assert common == 8
    assert seq == 'agccgatc'

    common, seq = lcs('COMPUTATION', 'INCEEMPUTABLE', do_print = True)
    assert common == 6
    assert seq == 'CMPUTA'

    common, seq = lcs('COMPUTATION', 'INCOMPUTABLE', do_print = True)
    assert common == 7
    assert seq == 'COMPUTA'

    common, seq = lcs('CAN', 'AB', do_print = True)
    assert common == 1
    assert seq == 'A'

    common, seq = lcs('ACGGA', 'ACTG', do_print = True)
    assert common == 3
    assert seq == 'ACG'
    
    dna1 = random_dna(100)
    dna2 = random_dna(100)
    common, seq = lcs(dna1, dna2, do_print = True)

    dna1 = random_dna(500)
    dna2 = random_dna(500)
    common, seq = lcs(dna1, dna2, do_print = True)

if __name__ == '__main__':
    test_lcs()