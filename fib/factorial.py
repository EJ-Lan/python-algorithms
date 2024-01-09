def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def test_factorial(n):
    print(f"The factorial of {n} is {factorial(n)}")

def test_all_factorial():
    test_factorial(0)
    test_factorial(1)
    test_factorial(10)
    test_factorial(500)

if __name__ == '__main__':
    test_all_factorial()
