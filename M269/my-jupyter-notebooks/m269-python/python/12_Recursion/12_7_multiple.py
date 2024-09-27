# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 12.7 Multiple recursion

### 12.7.1 Dividing the input

### 12.7.2 Designing multiple recursion

#### Exercise 12.7.1

#### Exercise 12.7.2

# CELL 1

from algoesup import test

def has(items: list, item: object) -> bool:
    """Return True if and only if item is a member of items."""

    def in_slice(start: int, end: int) -> bool:
        """Return True if and only if item is in slice items[start:end].

        Preconditions: 0 <= start <= end <= len(items)
        """
        pass

    return in_slice(0, len(items))

has_tests = [
    # case,         items,   item,  has?
    ('empty list',  [],         3,  False),
    ('last member', [1, 2, 3],  3,  True),
    ('not member',  [1, 2, 3],  4,  False),
]

test(has, has_tests)    # run against the same tests