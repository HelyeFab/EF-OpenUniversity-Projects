# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 11.2 Factorisation

# CELL 1

factorisation_tests = [
    # case,         n,  factors
    ('smallest n',  1,  {1}),
    ('2 factors',   2,  {1, 2}),
    ('3 factors',   25, {1, 5, 25}),
    ('4 factors',   10, {1, 2, 5, 10}),
    ('5+ factors',  40, {1, 2, 4, 10, 20, 40})
]

### 11.2.1 Make candidates explicit

# CELL 2

from algoesup import test

def factorisation(n: int) -> set:
    """Return all positive integer divisors of n.

    Preconditions: n > 0
    """
    factors = set()
    for candidate in range(1, n+1):
        if n % candidate == 0:
            factors.add(candidate)
    return factors

test(factorisation, factorisation_tests)

# CELL 3

factorisation_tests[-1] = ('5+ factors',  40, {1, 2, 4, 5, 8, 10, 20, 40})
test(factorisation, factorisation_tests)

### 11.2.2 Compute solutions

# CELL 4

def symmetric_factorisation(n: int) -> set:
    """Return all positive integer divisors of n.

    Preconditions: n > 0
    """
    factors = set()
    candidates = set(range(1, n+1))
    while len(candidates) > 0:
        candidate = candidates.pop()
        if n % candidate == 0:
            factors.add(candidate)
            factors.add(n // candidate)
            candidates.discard(n // candidate)
    return factors

test(symmetric_factorisation, factorisation_tests)

### 11.2.3 Sort candidates

# CELL 5

def root_factorisation(n: int) -> set:
    """Return all positive integer divisors of n.

    Preconditions: n > 0
    """
    factors = set()
    candidate = 1
    while candidate * candidate <= n:
        if n % candidate == 0:
            factors.add(candidate)
            factors.add(n // candidate)
        candidate = candidate + 1
    return factors

test(root_factorisation, factorisation_tests)

# CELL 6

from algoesup import time_functions_int

time_functions_int([factorisation, symmetric_factorisation, root_factorisation])

### 11.2.4 Prime numbers

#### Exercise 11.2.1

#### Exercise 11.2.2

#### Exercise 11.2.3 (optional)

# CELL 7

import math
from algoesup import test

def is_prime(n: int) -> bool:
    pass

prime_tests = [
    # case,         n,      is_prime
    ('smallest n',  1,      False),
    ('even prime',  2,      True),
    ('n = 4',       4,      False)
]

test(is_prime, prime_tests)