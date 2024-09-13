# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 13.4 Binary search

### 13.4.1 Recursive, with slicing

#### Algorithm

#### Exercise 13.4.1

#### Complexity

### 13.4.2 Recursive, without slicing

# CELL 1

def has(items: list, item: object) -> bool:
    """Return True if and only if item is a member of items.

    Preconditions:
    - items is in ascending order
    - item is comparable to all members of items
    """

    def in_slice(start: int, end: int) -> bool:
        """Return True if and only if item is in slice items[start:end].

        Preconditions: 0 <= start <= end <= len(items)
        """
        # print('Searching', item, 'in', items[start:end])
        if end == start:
            return False
        else:
            middle = start + (end - start) // 2
            middle_item = items[middle]
            if middle_item == item:
                return True
            elif item < middle_item:
                return in_slice(start, middle)
            else:
                return in_slice(middle + 1, end)

    return in_slice(0, len(items))

# CELL 2

from algoesup import test

has_tests = [
    # case,                 items,  item,   has?
    ('empty list',          [],     1,      False),
    ('is before 1 item',    [2],    1,      False),
    ('is the 1 item',       [1],    1,      True),
    ('is after 1 item',     [2],    3,      False),
    ('is before 2 items',   [2, 4], 1,      False),
    ('is between 2 items',  [2, 4], 3,      False),
    ('is after 2 items',    [2, 4], 5,      False),
    ('is 1st of 2 items',   [2, 4], 2,      True),
    ('is 2nd of 2 items',   [2, 4], 4,      True),
]

test(has, has_tests)

#### Exercise 13.4.2

### 13.4.3 Iterative

# CELL 3

def has_iterative(items: list, item: object) -> bool:
    start = 0
    end = len(items)
    while start < end:          # alternative: while start != end
        middle = start + (end - start) // 2
        middle_item = items[middle]
        if middle_item == item:
            return True
        elif item < middle_item:
            end = middle        # search left half [start:middle]
        else:
            start = middle + 1  # search right half [middle+1:end]
    return False

test(has_iterative, has_tests)

# CELL 4

items = [0] * 1_000_000_000     # a billion zeros

# %timeit -r 5 has(items, 1)
# %timeit -r 5 has_iterative(items, 1)