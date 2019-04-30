def fib(n):
    if n <= 1:
        return n
    else:
        f = fib(n-1) + fib(n-2)
    return f
