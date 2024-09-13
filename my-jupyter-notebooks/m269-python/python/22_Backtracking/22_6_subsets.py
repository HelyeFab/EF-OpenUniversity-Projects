# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 22.6 Generate subsets

# CELL 1

def extend(candidate: set, extensions: list, solutions: list) -> None:
    """Extend candidate with all subsets of extensions and add to solutions."""
    print('Visiting node', candidate, extensions)
    if len(extensions) == 0:    # complete candidate
        solutions.append(candidate)
    else:
        item = extensions[0]    # head of sequence
        rest = extensions[1:]   # tail of sequence
        extend(candidate.union({item}), rest, solutions) # add item
        extend(candidate, rest, solutions)               # skip item

# CELL 2

def all_subsets(n: int) -> list:
    """Return all subsets of 1, ..., n in the order generated."""
    candidate = set()
    extensions = list(range(1, n+1))
    solutions = []
    extend(candidate, extensions, solutions)
    return solutions

print('Subsets:', all_subsets(3))