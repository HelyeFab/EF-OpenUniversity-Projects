# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 12.6 Avoiding slicing

### 12.6.1 Problem definition

### 12.6.2 Recursive definition

#### Exercise 12.6.1

#### Exercise 12.6.2

### 12.6.3 Code

# CELL 1

from algoesup import test

def slice_has(items: list, item: object, start: int, end: int) -> bool:
    """Return True if and only if item is a member of slice items[start:end].

    Preconditions: 0 <= start <= end <= len(items)
    """
    if start == end:
        return False
    elif items[start] == item:
        return True
    else:
        return slice_has(items, item, start+1, end)

def has(items: list, item: object) -> bool:
    """Return True if and only if item is a member of items."""
    return slice_has(items, item, 0, len(items))

has_tests = [
    # case,         items,   item,  has?
    ('empty list',  [],         3,  False),
    ('last member', [1, 2, 3],  3,  True),
    ('not member',  [1, 2, 3],  4,  False),
]

test(has, has_tests)

# CELL 2

def has(items: list, item: object) -> bool:
    """Return True if and only if item is a member of items."""

    def in_slice(start: int, end: int) -> bool:
        """Return True if and only if item is in slice items[start:end].

        Preconditions: 0 <= start <= end <= len(items)
        """
        if start == end:
            return False
        elif items[start] == item:
            return True
        else:
            return in_slice(start+1, end)

    return in_slice(0, len(items))

test(has, has_tests)    # run against the same tests

#### Exercise 12.6.3

# CELL 3

from algoesup import test

def maximum(numbers: list) -> int:
    """Return the largest number in numbers.

    Preconditions: numbers is a non-empty list of integers
    """
    pass

maximum_tests = [
    # case,             numbers,       maximum
    ('shortest input',  [5],                5),
    ('all equal',       [-1, -1],          -1),
    ('ascending',       [-1, 0, 3],         3),
    ('descending',      [4, 2, 1],          4),
    ('unsorted',        [2, 4, 3, 4, 1],    4)
]

test(maximum, maximum_tests)