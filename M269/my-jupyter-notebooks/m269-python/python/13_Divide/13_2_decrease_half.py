# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 13.2 Decrease by half

### 13.2.1 Problem

# CELL 1

def power_by_one(base: int, exponent: int) -> int:
    """Return the base to the power of the exponent.

    Preconditions: exponent >= 0
    """
    if exponent == 0:
        return 1
    else:
        return power_by_one(base, exponent - 1) * base

power_by_one(3, 20) == 3 ** 20  # test with Python's power operator

### 13.2.2 Algorithm

### 13.2.3 Complexity

### 13.2.4 Code and performance

# CELL 2

def power_by_half(base: int, exponent: int) -> int:
    """Return the base to the power of the exponent.

    Preconditions: exponent >= 0
    """
    if exponent == 0:
        return 1
    else:
        subsolution = power_by_half(base, exponent // 2)
        if exponent % 2 == 0:
            return subsolution * subsolution
        else:
            return subsolution * subsolution * base

power_by_half(3, 20) == 3 ** 20

# CELL 3

exponent = 20
while exponent <= 200:
    # %timeit -r 5 -n 10_000 power_by_one(3, exponent)
    exponent = 2 * exponent

# CELL 4

exponent = 20
while exponent <= 200:
    # %timeit -r 5 -n 10_000 power_by_half(3, exponent)
    exponent = 2 * exponent