# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 24.4.7 answer

# CELL 1

def edit_bottomup(left: str, right: str) -> int:
    """Return the Levenshtein distance between the strings."""
    cache = []
    for l in range(len(left) + 1):
        cache.append([-1] * (len(right) + 1))

    for l in range(len(left), -1, -1):
        for r in range(len(right), -1, -1):
            if l == len(left):
                cache[l][r] = len(right) - r
            elif r == len(right):
                cache[l][r] = len(left) - l
            elif left[l] == right[r]:
                cache[l][r] = cache[l+1][r+1]
            else:
                delete = cache[l+1][r] + 1
                insert = cache[l][r+1] + 1
                replace = cache[l+1][r+1] + 1
                cache[l][r] = min(replace, delete, insert)

    return cache[0][0]