def recursive_fib(n: int) -> int:
    """ Recursively calculates the n^th fibonacci number """
    if n <= 1:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)

def iterative_fib(n: int) -> int:
    """  """ 
    if n <= 1:
        return n
    prev = 1
    fib = 1
    for i in range(2, n):
        temp = fib
        fib += prev
        prev = temp
    return fib

print(recursive_fib(6))
print(recursive_fib(7))
print(recursive_fib(8))
print(iterative_fib(6))
print(iterative_fib(7))
print(iterative_fib(8))
