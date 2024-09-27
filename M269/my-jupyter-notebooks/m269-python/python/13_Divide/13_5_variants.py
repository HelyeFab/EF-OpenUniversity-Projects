# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 13.5 Binary search variants

### 13.5.1 Transition

#### Exercise 13.5.1

# CELL 1

from algoesup import test

def first_positive(numbers: list) -> int:
    """Return the first (lowest index) positive integer in numbers.

    Preconditions:
    - numbers is a list of integers in ascending order
    - numbers has a positive integer
    """
    def in_slice(start: int, end: int) -> int:
        """Return the first positive number within numbers[start:end].

        Preconditions: 0 <= start < end <= len(items)
        """
        pass

    return in_slice(0, len(numbers))

first_positive_tests = [
    # case,             numbers,            first
    ('one number',      [1],                    1),
    ('is last',         [-2, -2, 0, 3],         3),
    ('all positive',    [2, 3, 4],              2),
    ('all but first',   [0, 1, 2, 2, 2, 2, 2],  1),
]

test(first_positive, first_positive_tests)

#### Exercise 13.5.2

# CELL 2

def first_positive(numbers: list) -> int:
    pass

test(first_positive, first_positive_tests)

### 13.5.2 Right number in the right place

#### Exercise 13.5.3