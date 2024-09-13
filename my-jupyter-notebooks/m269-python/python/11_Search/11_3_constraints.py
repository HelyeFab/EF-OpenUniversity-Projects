# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 11.3 Constraint satisfaction

### 11.3.1 Problem

### 11.3.2 Algorithm and complexity

### 11.3.3 Code and performance

# CELL 1

def equations(sum: int, product: int, square_sum: int) -> set:
    """Return all triples that satisfy the constraints.

    Preconditions: sum > 0, product > 0, square_sum > 0
    Postconditions: the output has exactly all (x, y, z) such that
    - x ≠ y ≠ z ≠ x and x, y, z are integers
    - x+y+z = sum, x*y*z = product, x² + y² + z² = square_sum
    """

    def satisfies(x: int, y: int, z: int) -> bool:
        """Check if x, y and z satisfy the constraints."""
        if x == y or y == z or z == x:
            return False
        if x + y + z != sum or x*y*z != product:
            return False
        return x*x + y*y + z*z == square_sum

    solutions = set()
    for x in range(-product, product+1):
        for y in range(-product, product+1):
            for z in range(-product, product+1):
                if satisfies(x, y, z):
                    solutions.add( (x, y, z) )
    return solutions

# CELL 2

equations(6, 6, 14)

# CELL 3

# %timeit -r 3 equations(6, 6, 14)

#### Exercise 11.3.1

# CELL 4

pass

# CELL 5

pass

### 11.3.4 Don't generate equivalent candidates

### 11.3.5 Reduce the range

### 11.3.6 Compute part of a candidate

### 11.3.7 Improved code and performance

# CELL 6

import math

def fast_equations(sum: int, product: int, square_sum: int) -> set:
    solutions = set()
    limit = min(product, math.floor(math.sqrt(square_sum)))
    for x in range(-limit, limit + 1):
        for y in range(x+1, limit + 1):
            z = sum - x - y
            if y < z and x*y*z == product and x*x+y*y+z*z == square_sum:
                solutions.add( (x, y, z) )
    return solutions

# CELL 7

print(fast_equations(6, 6, 14))
# %timeit -r 3 fast_equations(6, 6, 14)

# CELL 8

print(fast_equations(0, 6, 14))
# %timeit -r 3 fast_equations(0, 6, 14)

# CELL 9

print(fast_equations(21, 336, 149))
# %timeit -r 3 fast_equations(21, 336, 149)

# CELL 10

print(fast_equations(33, 1320, 365))
# %timeit -r 3 fast_equations(33, 1320, 365)