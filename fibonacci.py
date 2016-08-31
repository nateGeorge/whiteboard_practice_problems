def fib(x):
    if not isinstance(x, int):
        print "argument must be an integer"
        return
    if x == 0:
        return 0
    a, b = 0, 1
    for i in range(x-1):
        a, b = b, a + b
    return b

def fib_rec(x):
    if not isinstance(x, int):
        raise ValueError("argument must be an integer") # another way to alert the user
    if x > 1:
        return fib_rec(x - 1) + fib_rec(x - 2)
    return x
