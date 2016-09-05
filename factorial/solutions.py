# smart-ass answer
import math
def fac(n):
    return math.factorial(n)

# one-liner
import operator as op
def fac(n):
    return reduce(op.mul, range(1, n+1))

# for loop
def fac(n):
    ans = 1
    for i in range(1, n + 1):
        ans *= i

    return ans

# recursive
def fac(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("arg must be positive")
    if not isinstance(n, int):
        raise ValueError("arg must be int")
    return fac(n-1)*n
