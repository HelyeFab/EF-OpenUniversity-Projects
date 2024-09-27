# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 22.4 Optimise

### 22.4.1 The problem

# CELL 1

def sum(numbers: list) -> int:
    """Return the sum of the numbers."""
    total = 0
    for number in numbers:
        total = total + number
    return total

### 22.4.2 Keep the best

# CELL 2

SOLUTION = 0
VALUE = 1

# CELL 3

def extend(candidate: list, extensions: set, n: int, best: list) -> None:
    """Update best if needed, and extend candidate."""
    print('Visiting node', candidate, extensions)
    if satisfies_range(candidate, n):
        candidate_value = sum(candidate)
        if candidate_value < best[VALUE]:
            print('New best', candidate, 'with value', candidate_value)
            best[SOLUTION] = candidate
            best[VALUE] = candidate_value
    for item in extensions:
        if can_extend(item, candidate):
            extend(candidate + [item], extensions - {item}, n, best)

# CELL 4

def best_sequence(n: int) -> list:
    """Return a lowest sum sequence that satisfies both constraints."""
    candidate = []
    extensions = set(range(1, n+1))
    solution = list(range(1, n+1))
    best = [solution, sum(solution)]
    extend(candidate, extensions, n, best)
    return best

# CELL 5

def satisfies_range(candidate: list, n: int) -> bool:
    """Check if first and last numbers in candidate are at least n/2 apart.

    Preconditions: candidate is a list of integers; n > 2
    """
    return len(candidate) > 1 and abs(candidate[0] - candidate[-1]) >= n / 2

def can_extend(item: int, candidate: list) -> bool:
    """Check if extending candidate with item can lead to a solution."""
    # the number and the index where it will be put must have different parity
    return item % 2 != len(candidate) % 2

best_sequence(4)

### 22.4.3 Avoid worse candidates

# CELL 6

def can_extend(item: int, candidate: list, best: list) -> bool:
    """Check if item can extend candidate to a better solution than best."""
    return item % 2 != len(candidate) % 2 and item + sum(candidate) < best[VALUE]

# CELL 7

def extend(candidate: list, extensions: set, n: int, best: list) -> None:
    """Update best if a better extension of candidate is found."""
    print('Visiting node', candidate, extensions)
    if satisfies_range(candidate, n):
        candidate_value = sum(candidate)
        if candidate_value < best[VALUE]:
            print('New best', candidate, 'with value', candidate_value)
            best[SOLUTION] = candidate
            best[VALUE] = candidate_value
    for item in extensions:
        if can_extend(item, candidate, best):   # changed line
            extend(candidate + [item], extensions - {item}, n, best)

best_sequence(4)

### 22.4.4 Start well

# CELL 8

def best_sequence(n: int) -> list:
    """Return a lowest sum sequence that satisfies both constraints."""
    candidate = []
    extensions = set(range(1, n+1))
    if n % 2 == 0:              
        solution = [1, n]
    else:
        solution = [1, 2, n]
    best = [solution, sum(solution)]
    extend(candidate, extensions, n, best)
    return best

best_sequence(4)