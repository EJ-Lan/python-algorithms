# returns pair (result, number of multiplications)
def power(b,n):
    assert n >= 0
    if n == 0: return 1, 0
    if n%2 == 1:
        a, mul = power(b, n-1)
        return a*b, mul + 1
    else:
        n2 = n//2
        a, mul = power(b, n2)
        return a*a, mul + 1
    
def test_power_case(n):
    b=2
    result, mul = power(b, n)
    assert result == pow(b, n) # pow = Python built-in power function
    print(f'computed {b}^{n} with {mul} multiplications')

def test_power():
    print('Test fast exponentiation')
    test_power_case(50)
    test_power_case(63)
    test_power_case(64)
    test_power_case(1<<19) # best case about log n
    test_power_case((1<<20)-1) # worst case about 2 log n
    test_power_case(1<<20) # best case about log n
    
if __name__ == '__main__':
    test_power()