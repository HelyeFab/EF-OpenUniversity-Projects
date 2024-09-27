# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 22.2 Prune the search space

# CELL 1

def satisfies_range(candidate: list, n: int) -> bool:
    """Check if first and last numbers in candidate are at least n/2 apart.

    Preconditions: candidate is a list of integers; n > 2
    """
    return len(candidate) > 1 and abs(candidate[0] - candidate[-1]) >= n / 2

def satisfies_parity(candidate: list) -> bool:
    """Check if candidate is an odd, even, odd, ... sequence.

    Preconditions: candidate is a list of integers
    """
    for index in range(len(candidate)):
        if index % 2 == candidate[index] % 2:
            return False
    return True

### 22.2.1 Local and global constraints

# CELL 2

def extend(candidate: list, extensions: set, n: int, solutions: list) -> None:
    """Add to solutions all valid permutations that extend candidate.

    Preconditions: n > 2 and
    - candidate is a list of integers between 1 and n
    - extensions is a set of integers between 1 and n
    - candidate and extensions have no integer in common
    """
    print('Visiting node', candidate, extensions)
    # base case 1: backtrack
    if not satisfies_parity(candidate):
        return
    # base case 2: candidate is solution
    # local constraint is satisfied, so only check global constraint
    if satisfies_range(candidate, n):
        solutions.append(candidate)
    for item in extensions:
        extend(candidate + [item], extensions - {item}, n, solutions)

# CELL 3

def valid_permutations(n: int) -> list:
    """Return all valid permutations of 1, ..., n in the order generated."""
    candidate = []
    extensions = set(range(1, n+1)) # {1, ..., n}
    solutions = []
    extend(candidate, extensions, n, solutions)
    return solutions

print('Solutions:', valid_permutations(3))

### 22.2.2 Avoid visits

# CELL 4

def extend(candidate: list, extensions: set, n: int, solutions: list) -> None:
    print('Visiting node', candidate, extensions)
    if satisfies_range(candidate, n):
        solutions.append(candidate)
    for item in extensions:
        if can_extend(item, candidate):     # added line
            extend(candidate + [item], extensions - {item}, n, solutions)

# CELL 5

def can_extend(item: int, candidate: list) -> bool:
    """Check if extending candidate with item can lead to a solution."""
    # the number and the index where it will be must have different parity
    return item % 2 != len(candidate) % 2

valid_permutations(3)