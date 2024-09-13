# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 12.4 Inspecting sequences

### 12.4.1 Maximum

#### Exercise 12.4.1

# CELL 1

from algoesup import test

# %run -i ../m269_rec_list

def maximum(numbers):
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

### 12.4.2 Membership

# CELL 2

# %run -i ../m269_rec_list

def has(items: list, item: object) -> bool:
    """Return True if and only if item is a member of items."""
    if is_empty(items):
        return False
    elif head(items) == item:
        return True
    else:
        return has(tail(items), item)

has([1, 3, -1], 2)

#### Exercise 12.4.2

### 12.4.3 Indexing

#### Exercise 12.4.3

# CELL 3

from algoesup import test

# %run -i ../m269_rec_list

pass

# test(value, value_tests)