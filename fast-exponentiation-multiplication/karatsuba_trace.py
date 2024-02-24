import random

def split(x, n): # returns two about n/2 bit numbers
    assert x >= 1
    assert x.bit_length() <= n
    left  = x >> n // 2
    right = x - (left << n // 2) # slow, could be faster with low-level access
    assert right < 1 << (n // 2)
    print("split", x.bit_length(), "bit number", bin(x))
    print("into", bin(left), "and", bin(right))
    assert left.bit_length() <= (n + 1) // 2
    assert right.bit_length() <= n // 2
    assert left * pow(2, n // 2) + right == x
    return left, right

def multiply(x, y):
    assert x >= 0
    assert y >= 0
    xbits = x.bit_length()
    ybits = y.bit_length()
    n = max(xbits, ybits)
    print("multiply", bin(x), "with", bin(y))
    limit = 8 # Use direct multiply for small numbers
    if n <= limit:
        print(f'both numbers at most {limit} bits, use direct multiplication')
        print(f'{bin(x)} * {bin(y)} = {bin(x*y)}')
        return x * y
    xl, xr = split(x, n)
    yl, yr = split(y, n)
    r1 = multiply(xl, yl)
    r3 = multiply(xr, yr)
    r2 = multiply(xl + xr, yl + yr) - r1 - r3 # Gauss trick
    n2 = n // 2
    return (r1 << (2 * n2)) + (r2 << n2) + r3

def test_multiply():
# This test takes about 2 seconds on my laptop
    for n in range(20,22):
        x = random.randrange(1 << n) # random number up to n-1 bits
        y = random.randrange(1 << n)
        m = multiply(x,y)
        assert m == x*y # compare with Python's built-in multiply

if __name__ == '__main__':
    test_multiply()