# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 22.1 Generate sequences

# CELL 1

def satisfies_range(numbers: list, n: int) -> bool:
    """Check if first and last of numbers are at least n/2 apart.

    Preconditions:
    - numbers is a list of integers; len(numbers) >= 2
    - n > 2
    """
    return abs(numbers[0] - numbers[-1]) >= n / 2

# CELL 2

def satisfies_parity(numbers: list) -> bool:
    """Check if numbers is an odd, even, odd, ... sequence.

    Preconditions: numbers is a list of integers
    """
    for index in range(len(numbers)):
        if index % 2 == numbers[index] % 2:
            return False
    return True

# CELL 3

def is_solution(permutation: list, n: int) -> bool:
    """Check if permutation satisfies the range and parity constraints.

    Preconditions: n > 2 and permutation is a rearrangement of 1, ..., n
    """
    return satisfies_range(permutation, n) and satisfies_parity(permutation)

### 22.1.1 Recursive generation

# CELL 4

def extend(candidate: list, extensions: set, n: int, solutions: list) -> None:
    """Add to solutions all valid permutations that extend candidate.

    Preconditions: n > 2 and
    - candidate is a list of integers between 1 and n
    - extensions is a set of integers between 1 and n
    - candidate and extensions have no integer in common
    """
    print('Visiting node', candidate, extensions)
    if len(extensions) == 0:    # leaf node: candidate is complete
        print('Testing candidate', candidate)
        if is_solution(candidate, n):
            solutions.append(candidate)
    else:                       # create and visit children nodes
        for item in extensions:
            extend(candidate + [item], extensions - {item}, n, solutions)

# CELL 5

def valid_permutations(n: int) -> list:
    """Return all valid permutations of 1, ..., n in the order generated."""
    candidate = []
    extensions = set(range(1, n+1))     # {1, ..., n}
    solutions = []
    extend(candidate, extensions, n, solutions)
    return solutions

print('Solutions:', valid_permutations(3))

### 22.1.2 Accept partial candidates

# CELL 6

def extend(candidate: list, extensions: set, n: int, solutions: list) -> None:
    if is_solution(candidate, n):
        solutions.append(candidate)
    for item in extensions:
        extend(candidate + [item], extensions - {item}, n, solutions)

# CELL 7

def satisfies_range(numbers: list, n: int) -> bool:
    """Check if first and last of numbers are at least n/2 apart.

    Preconditions: numbers is a list of integers; n > 2
    """
    return len(numbers) > 1 and abs(numbers[0] - numbers[-1]) >= n / 2

# CELL 8

valid_permutations(4)