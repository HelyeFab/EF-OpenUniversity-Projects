# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.7 Reversal

### 4.7.1 Problem definition

### 4.7.2 Problem instances

# CELL 1

reversed_list_tests = [
    # case,             values,             reversed
    ('empty list',      [],                 []              ),
    ('length 1',        [4],                [4]             ),
    ('length 2',        [5, True],          [True, 5]       ),
    ('length 5',        [5, 6, 7, 8, 9],    [9, 8, 7, 6, 5] ),
    ('same items',      [0, 0, 0],          [0, 0, 0]       )
]

### 4.7.3 Algorithm

### 4.7.4 Complexity

### 4.7.5 Code

# CELL 2

def reversed_list(values: list) -> list:
    """Return the same items as values, in inverse order.

    Postconditions: the output is
    [values[-1], values [-2], ..., values[1], values[0]]
    """
    reversed = []
    for item in values:
        reversed.insert(0, item)
    return reversed

### 4.7.6 Tests

# CELL 3

def test_reversed_list(test_table: list) -> None:
    """Report which tests for the reversed_list function fail."""
    for test_case in test_table:
        name = test_case[0]
        values = test_case[1]
        reversed = test_case[2]
        actual = reversed_list(values)
        if actual != reversed:
            print(name, 'FAILED:', actual, 'instead of', reversed)
    print('Tests finished.')

# CELL 4

test_reversed_list(reversed_list_tests)

# CELL 5

import algoesup

algoesup.test(reversed_list, reversed_list_tests)

# CELL 6

from algoesup import test

test(reversed_list, reversed_list_tests)

### 4.7.7 Performance

# CELL 7

size = 10
for measurement in range(10):
    numbers = list(range(size))     # list [0, 1, 2, ..., size-1]
    print('Reversing', size, 'numbers:')
    # %timeit -r 5 reversed_list(numbers)
    size = size * 2

#### Exercise 4.7.1

#### Exercise 4.7.2

#### Exercise 4.7.3

# CELL 8

def reversed_list_2(values: list) -> list:
    """Return the same items as values, in inverse order.

    This is a more efficient version of reversed_list.
    Postconditions: the output is
    [values[-1], values [-2], ..., values[1], values[0]]
    """
    # replace with your function body

test(reversed_list_2, reversed_list_tests)

#### Exercise 4.7.4

#### Exercise 4.7.5

#### Exercise 4.7.6

#### Exercise 4.7.7

# CELL 9

def reverse_in_place(values: list) -> None:
    """Write the docstring."""
    # replace with your code

def test_reverse_in_place(test_table: list) -> None:
    """Report which tests for the reverse_in_place function fail."""
    for test_case in test_table:
        name = test_case[0]
        values = test_case[1]
        reversed = test_case[2]
        reverse_in_place(values)
        if values != reversed:
            print(name, 'FAILED:', values, 'instead of', reversed)
    print('Tests finished.')

test_reverse_in_place(reversed_list_tests)