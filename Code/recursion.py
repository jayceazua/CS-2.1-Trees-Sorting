#!python
from functools import lru_cache

def fibonacci(n):
    """fibonacci(n) returns the n-th number in the Fibonacci sequence,
    which is defined with the recurrence relation:
    fibonacci(0) = 0
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2), for n > 1"""
    # Check if n is negative or not an integer (invalid input)
    if n < 0 or not isinstance(n, int):
        raise ValueError('fibonacci is undefined for n = {!r}'.format(n))
    # Implement fibonacci_recursive, _memoized, and _dynamic below, then
    # change this to call your implementation to verify it passes all tests
    # return fibonacci_recursive(n)
    # return fibonacci_memoized(n)
    return fibonacci_dynamic(n)


def fibonacci_recursive(n):
    # Check if n is one of the base cases
    if n == 0 or n == 1:
        return n
    # Check if n is larger than the base cases
    elif n > 1:
        # Call function recursively and add the results together
        return fibonacci_recursive(n - 1) + \
            fibonacci_recursive(n - 2)

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    # TODO: Memoize the fibonacci function's recursive implementation here
    # Once implemented, change fibonacci (above) to call fibonacci_memoized
    # to verify that your memoized implementation passes all test cases
    if n == 0 or n == 1:
        return n
    
    return fibonacci_memoized(n - 1) + \
        fibonacci_memoized(n - 2)


def fibonacci_dynamic(n):
    # TODO: Implement the fibonacci function with dynamic programming here
    pass
    # Once implemented, change fibonacci (above) to call fibonacci_dynamic
    # to verify that your dynamic implementation passes all test cases
    if n < 2:
        return n
    
    n_1 = 1
    n_2 = 0
    res = 0

    i = 2

    while i <= n:
        res = n_1 + n_2

        n_2 = n_1
        n_1 = res
        i += 1
    
    return res
    


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 1:
        num = int(args[0])
        result = fibonacci(num)
        print('fibonacci({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))


if __name__ == '__main__':
    main()
