# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 22.7 Back to the knapsack

# CELL 1

ITEMS = {(1, 2), (2, 3), (3, 4), (4, 20), (5, 30)}

### 22.7.1 The problem

### 22.7.2 The value function

# CELL 2

WEIGHT = 0
VALUE = 1

def value(items: set) -> int:
    """Return the total value of the items."""
    total = 0
    for item in items:
        total = total + item[VALUE]
    return total

### 22.7.3 The constraints functions

# CELL 3

def can_extend(item: tuple, candidate: set, capacity: int) -> bool:
    """Check if adding the item to candidate won't exceed the capacity."""
    total = item[WEIGHT]
    for another_item in candidate:
        total = total + another_item[WEIGHT]
    return total <= capacity

### 22.7.4 The backtracking function

# CELL 4

SOLUTION = 0
VALUE = 1

def extend(candidate: set, extensions: list, capacity: int, best: list) -> None:
    """Update best if candidate is a better solution, then try to extend it."""
    print('Visiting node', candidate, extensions)
    if len(extensions) == 0:
        candidate_value = value(candidate)
        if candidate_value > best[VALUE]:
            print('New best with value', candidate_value)
            best[SOLUTION] = candidate
            best[VALUE] = candidate_value
    else:
        item = extensions[0]
        rest = extensions[1:]
        if can_extend(item, candidate, capacity):
            extend(candidate.union({item}), rest, capacity, best)
        extend(candidate, rest, capacity, best)

### 22.7.5 The main function

# CELL 5

def knapsack(items: set, capacity: int) -> list:
    """Return a subset of items and their total value.

    Preconditions:
    - items is a set of weight-value pairs, both integers
    - no integer is negative
    Postconditions:
    - the output is a set-integer pair
    - total weight of the output items <= capacity
    - no other subset of items has higher value and fits the capacity
    """
    candidate = set()
    extensions = list(items)
    solution = set()
    best = [solution, value(solution)]
    extend(candidate, extensions, capacity, best)
    return best

# CELL 6

knapsack(ITEMS, 4)

### 22.7.6 Sort extensions

# CELL 7

def knapsack(items: set, capacity: int) -> list:
    candidate = set()
    extensions = sorted(items)  # changed line
    solution = set()
    best = [solution, value(solution)]
    extend(candidate, extensions, capacity, best)
    return best

# CELL 8

def extend(candidate: set, extensions: list, capacity: int, best: list) -> None:
    """Update best if candidate is a better solution, then try to extend it."""
    print('Visiting node', candidate, extensions)
    candidate_value = value(candidate)
    if candidate_value > best[VALUE]:
        print('New best with value', candidate_value)
        best[SOLUTION] = candidate
        best[VALUE] = candidate_value
    if len(extensions) > 0:                         # changed line
        item = extensions[0]
        rest = extensions[1:]
        if can_extend(item, candidate, capacity):
            extend(candidate.union({item}), rest, capacity, best)
            extend(candidate, rest, capacity, best) # changed line

# CELL 9

knapsack(ITEMS, 4)

#### Exercise 22.7.1