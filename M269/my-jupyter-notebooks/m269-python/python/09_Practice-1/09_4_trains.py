# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 9.4 Trains

# CELL 1

from algoesup import test

def rearrange(wagons: int, outgoing: list) -> bool:
    """Can the incoming train be rearranged into outgoing?

    Preconditions:
    - wagons > 0
    - outgoing is a permutation of the numbers from 1 to wagons
    """
    pass

rearrange_tests = [
    # case,             wagons, outgoing,       rearrange?
    ['keep order',      3,      [1, 2, 3],          True],
    ['invert',          3,      [3, 2, 1],          True],
    ['swap',            3,      [1, 3, 2],          True],
    ['move to front',   5,      [5, 1, 2, 3, 4],    False],
    # new tests:
]

test(rearrange, rearrange_tests)

### 9.4.1 Problem definition

#### Exercise 9.4.1

#### Exercise 9.4.2

### 9.4.2 Algorithm and complexity

#### Exercise 9.4.3

#### Exercise 9.4.4

### 9.4.3 Code and tests

#### Exercise 9.4.5