# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 23.1 Fibonacci

# CELL 1

from algoesup import test

fibonacci_tests = [
    # case,     n,  n-th Fibonacci number
    ('n = 1',   1,  1),
    ('n = 2',   2,  1),
    ('n = 6',   6,  8),
    ('n = 10', 10, 55)
]

### 23.1.1 Recursive

# CELL 2

def fibonacci_rec(n: int) -> int:
    """Return the n-th Fibonacci number, computed recursively.

    Preconditions: n > 0
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

test(fibonacci_rec, fibonacci_tests)

# CELL 3

for n in range(20, 25):
    # %timeit -r 3 fibonacci_rec(n)

### 23.1.2 Top-down

# CELL 4

def fibonacci_td(n: int) -> int:
    def fib(n: int) -> int:
        """Cached version of fibonacci()."""
        if n not in cache:
            if n == 1 or n == 2:
                cache[n] = 1
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    cache = dict()
    return fib(n)

test(fibonacci_td, fibonacci_tests)

# CELL 5

for n in (8, 16, 32, 64):
    # %timeit -r 3 fibonacci_td(n)

### 23.1.3 Bottom-up

# CELL 6

def fibonacci_bu(n: int) -> int:
    # create cache with base cases fibonacci(1) = fibonacci(2) = 1
    cache = {1: 1, 2: 1}
    for number in range(3, n+1):
        cache[number] = cache[number-1] + cache[number-2]
    return cache[n]

test(fibonacci_bu, fibonacci_tests)

# CELL 7

for n in (8, 16, 32, 64):
    # %timeit -r 3 fibonacci_bu(n)

### 23.1.4 With arrays

# CELL 8

def fibonacci_tda(n: int) -> int:
    def fib(n: int) -> int:
        if cache[n] == 0:   # changed
            if n == 1 or n == 2:
                cache[n] = 1
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    cache = [0] * (n+1)     # changed
    return fib(n)

test(fibonacci_tda, fibonacci_tests)

# CELL 9

def fibonacci_bua(n: int) -> int:
    cache = [0] * (n+1)
    cache[1] = 1        # first base case
    if n > 1:
        cache[2] = 1    # second base case
    for number in range(3, n+1):
        cache[number] = cache[number-1] + cache[number-2]
    return cache[n]

test(fibonacci_bua, fibonacci_tests)

# CELL 10

from algoesup import time_functions_int

time_functions_int([
    fibonacci_rec, fibonacci_td, fibonacci_tda, fibonacci_bu, fibonacci_bua
    ], double=4)

### 23.1.5 A graph perspective