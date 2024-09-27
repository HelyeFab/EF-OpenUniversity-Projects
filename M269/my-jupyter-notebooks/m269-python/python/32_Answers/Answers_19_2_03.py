# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 19.2.3 answer

# CELL 1

from algoesup import test

def min_dot_product(x: list, y: list) -> int:
    """Return the smallest dot product over all permutations of x and y.

    Preconditions:
    x and y are non-empty lists of integers of the same length
    """
    x_up = sorted(x)
    y_down = sorted(y, reverse=True)
    product = 0
    for index in range(len(x)):
        product = product + x_up[index] * y_down[index]
    return product

min_dot_product_tests = [
    # case,        x,                 y,              smallest
    ('n = 3',      [1, 2, -1],        [2, 6, 3],           1),
    ('n = 5',      [1, -1, 5, 0, 7],  [3, 7, -9, 2, 0],  -68),
    # your tests
    ('n = 1',      [4],               [-3],              -12),
    ('x same',     [1, 1, 1],         [2, 4, 3],           9),
    ('x up, y up', [1, 2, 3, 4],      [-1, 0, 5, 7],      13),
]

test(min_dot_product, min_dot_product_tests)