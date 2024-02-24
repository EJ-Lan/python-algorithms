import random
import time

def split(x, n): # returns two about n/2 bit numbers
    assert x >= 1
    nx = x.bit_length()
    assert nx <= n
    left  = x >> n//2
    right = x - (left << n//2) # slow, could be faster with low-level access
    assert right < 1 << (n//2)
    #print ("split", bin(x), "into", bin(left), bin(right))
    assert left.bit_length() <= (n + 1)//2
    assert right.bit_length() <= n//2
    assert left * pow(2, n//2) + right == x
    return left, right

def multiply(x,y):
    #print(bin(x),bin(y))
    assert x >= 0
    assert y >= 0
    xbits = x.bit_length()
    ybits = y.bit_length()
    n = max(xbits, ybits)
    limit = 32 # Use direct multiply for small numbers
    if n <= limit:
        return x * y
    xl,xr = split(x, n)
    yl,yr = split(y, n)
    r1 = multiply(xl, yl)
    r3 = multiply(xr,yr)
    r2 = multiply(xl+xr, yl+yr) - r1 - r3 # Karatsuba's trick
    n2 = n//2 # floor(n/2) in integer arithmetic
    return (r1 << (2*n2)) + (r2 << n2) + r3

def test_multiply():
# This test takes about 2 seconds on my laptop
    print('Test the Karatsuba algorithm')
    last_time = 0
    for k in range(2, 16):
        n = 1<<k
        start_time = time.time()
        for _ in range(2): # repeat each test 2 times
            x = random.randrange(1 << n) # random number up to n-1 bits
            y = random.randrange(1 << n)
            m = multiply(x,y)
            #assert m == x*y # compare with Python's built-in multiply
        time_used = time.time() - start_time
        print (f'Length in bits {n} time {time_used:.3f}')
        if last_time > 0:
            print (f'Ratio {(time_used / last_time):.3f}')
        last_time = time_used

def test_multiply_builtin():
    print('Test Python builtin multiplication algorithm')
    last_time = 0
    for k in range(2, 20):
        n = 1<<k
        start_time = time.time()
        for _ in range(10): # repeat each test 10 times
            x = random.randrange(1 << n) # random number up to n-1 bits
            y = random.randrange(1 << n)
            m = x * y
        time_used = time.time() - start_time
        print (f'Length in bits {n} time {time_used:.3f}')
        if last_time > 0:
            print (f'Ratio {(time_used / last_time):.3f}')
        last_time = time_used

if __name__ == '__main__':
    test_multiply()
    test_multiply_builtin()