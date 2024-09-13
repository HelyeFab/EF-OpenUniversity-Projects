# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 24.5 Higher and higher

# CELL 1

from algoesup import test

higher_tests = [
    # case                  grid                        length
    ('one longest path',    [[10,7,10], [3,90,82]],     4),
    ('all numbers equal',   [[2, 2], [2, 2]],           1),
    ('go around grid',      [[2,3], [1,4], [6,5]],      6),
    ('two longest paths',   [[6,7,8],[6,5,4],[3,2,1]],  5)
]

### 24.5.1 Exercises

#### Exercise 24.5.1

#### Exercise 24.5.2

#### Exercise 24.5.3

# CELL 2

def higher(grid: list) -> int:
    """Return the length of the longest path of ascending numbers in grid.

    Preconditions: grid is a table of non-negative integers
                   with r > 0 rows and c > 0 columns
    """
    pass

test(higher, higher_tests)

#### Exercise 24.5.4

#### Exercise 24.5.5 (optional)

# CELL 3

def higher(grid: list) -> int:
    """Return the length of the longest path of ascending numbers in grid.

    Preconditions: grid is a table of non-negative integers
                   with r > 0 rows and c > 0 columns
    """
    pass


test(higher, higher_tests)