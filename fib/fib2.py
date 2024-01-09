from test_fibonacci import test_fibonacci

def fib2(n):
    f = [0] * (n + 1)
    f[0] = 0
    if n > 0:
        f[1] = 1
    for j in range(3, n + 1):
        f[j] = f[j- 1] + f[j - 2]
    return f[n]

def test_fib2():
    for n in range(100):
        test_fibonacci(n, fib2)

if __name__ == '__main__':
    test_fib2()