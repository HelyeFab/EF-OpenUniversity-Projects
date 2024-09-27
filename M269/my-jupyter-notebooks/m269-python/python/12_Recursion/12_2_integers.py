# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 12.2 Recursion on integers

### 12.2.1 Algorithm

### 12.2.2 Recursive definition

#### Exercise 12.2.1

#### Exercise 12.2.2

# CELL 1

from algoesup import test

def even(n: int) -> bool:
    """Write the docstring here."""
    pass

even_tests = [
    # case,             n,      even?
    ('smallest even',   2,      True),
    ('larger even',     100,    True),
    # your tests here
]

test(even, even_tests)