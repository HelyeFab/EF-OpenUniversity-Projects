# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 12.5 Creating sequences

### 12.5.1 Prepend

# CELL 1

# this code is also in m269_rec_list.py

def prepend(item: object, items: list) -> list:
    """Return a new list with item as head and items as tail."""
    return [item] + items

### 12.5.2 Linear search

#### Exercise 12.5.1

# CELL 2

from algoesup import test

# %run -i ../m269_rec_list

def positive(numbers: list) -> list:
    """Return a new list of all positive numbers in the input.

    Preconditions: all elements of numbers are integers or floats
    Postconditions:
    the output's elements are in the same order as in the input
    """
    pass

positive_tests = [
    # case,             numbers,        positive
    ('shortest input',  [],             []),
    # new tests:
]

test(positive, positive_tests)

### 12.5.3 Append and insert

#### Exercise 12.5.2

#### Exercise 12.5.3