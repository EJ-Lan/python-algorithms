from test_fibonacci import test_fibonacci

def fib1(n):
    if(n < 2):
        return n
    else:
        return fib1(n - 1) + fib1(n - 2)
    
if __name__ == '__main__':
    for n in range(100):
        test_fibonacci(n, fib1)