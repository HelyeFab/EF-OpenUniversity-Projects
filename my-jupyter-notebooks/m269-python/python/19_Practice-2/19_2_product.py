# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 19.2 Dot product

### 19.2.1 Exercises

#### Exercise 19.2.1

#### Exercise 19.2.2

#### Exercise 19.2.3

# CELL 1

from algoesup import test

def min_dot_product(x, y):
    pass

min_dot_product_tests = [
    # case,        x,                 y,              smallest
    ('n = 3',      [1, 2, -1],        [2, 6, 3],           1),
    ('n = 5',      [1, -1, 5, 0, 7],  [3, 7, -9, 2, 0],  -68),
    # your tests
]

test(min_dot_product, min_dot_product_tests)