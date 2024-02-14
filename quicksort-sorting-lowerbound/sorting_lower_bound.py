import math

factorial = 1
for n in range(2,101):
    factorial *= n
    v1 = math.log(factorial, 2)
    v2 = n * math.log(n, 2)
    print(f'n = {n}, log(n!) = {v1}, n log n = {v2}, ratio = {v1/v2}')