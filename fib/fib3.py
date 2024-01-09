from test_fibonacci import test_fibonacci

def fib3(n):
    if n == 0:
        return 0
    x , y = 0, 1
    for _ in range(n - 1):
        x, y = y , x + y
    return y

def test_fib3():
    for n in range(100):
        test_fibonacci(n, fib3)

if __name__ == '__main__':
    test_fib3()