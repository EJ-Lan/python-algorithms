import time

def test_fibonacci(n, fibonacci_function):
    start = time.time()
    fn = fibonacci_function(n)
    stop = time.time()
    print(f"fibonacci({n}) = {fn}, time used = {(stop - start):.2f}s")