# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 23.3 Knapsack

# CELL 1

from algoesup import test

WEIGHT = 0
VALUE = 1

def weight(items: list) -> int:
    """Return the total weight of the items."""
    total = 0
    for item in items:
        total = total + item[WEIGHT]
    return total

def value(items: list) -> int:
    """Return the total value of the items."""
    total = 0
    for item in items:
        total = total + item[VALUE]
    return total

ITEMS = [(2, 3), (2, 4), (3, 4), (4, 20), (5, 30)]
knapsack_tests = [
    # case,         items,  capacity,   knapsack
    ('none fits',   ITEMS,  1,          []),
    ('all fit',     ITEMS,  16,         ITEMS),
    ('one is best', ITEMS,  6,          [(5, 30)])
]

### 23.3.1 Recursive

# CELL 2

def knapsack(items: list, capacity: int) -> list:
    """Return a highest-value subsequence of items that weigh at most capacity.

    Preconditions:
    - items is a list of weight-value pairs, both positive integers
    - capacity ≥ 0
    """
    if len(items) == 0 or capacity == 0:
        return []
    else:
        item = items[0]     # head
        rest = items[1:]    # tail
        skip = knapsack(rest, capacity)
        # if item doesn't fit, we must skip it
        if item[WEIGHT] > capacity:
            return skip
        # otherwise take it if that leads to a higher value
        else:
            take = [item] + knapsack(rest, capacity - item[WEIGHT])
            if value(skip) > value(take):
                return skip
            else:
                return take

test(knapsack, knapsack_tests)

#### Exercise 23.3.1

# CELL 3

def knapsack_indices(items: list, capacity: int) -> list:
    # docstring not repeated

    def knapsack(index: int, capacity: int) -> list:
        """Return a subsequence of items[index:] that
        fits the capacity and maximises the value.

        Preconditions: 0 ≤ index ≤ len(items) and 0 ≤ capacity
        """
        pass

    pass    # call the auxiliary function and return the solution

test(knapsack_indices, knapsack_tests)

### 23.3.2 Common subproblems

#### Exercise 23.3.2

### 23.3.3 Top-down and bottom-up

#### Exercise 23.3.3

# CELL 4

def knapsack_topdown(items: list, capacity: int) -> list:
    def knapsack(index: int, capacity: int) -> list:
        """Return a subsequence of items[index:] that
        fits the capacity and maximises the value.

        Preconditions: 0 ≤ index ≤ len(items) and 0 ≤ capacity
        """
        pass

    pass    # create an empty cache and call the auxiliary function

# CELL 5

knapsack_topdown([(1, 3), (1, 4), (3, 4), (4, 20)], 4)

# CELL 6

test(knapsack_topdown, knapsack_tests)

#### Exercise 23.3.4

# CELL 7

def knapsack_bottomup(items: list, capacity: int) -> list:
    # create the cache
    # for each row from last to first:
        # for each column:
            # compute cache[row][column]
    pass # return the cell with the solution for items and capacity

test(knapsack_bottomup, knapsack_tests)

### 23.3.4 Complexity