# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 24.4.5 answer

# CELL 1

def edit_topdown(left: str, right: str) -> int:
    """Return the Levenshtein distance between the strings."""

    def edit(l: int, r: int) -> int:
        """Return the Levenshtein distance of left[l:] and right[r:].

        Preconditions: 0 ≤ l ≤ len(left) and 0 ≤ r ≤ len(right)
        """
        if cache[l][r] == -1:
            if l == len(left):
                cache[l][r] = len(right) - r
            elif r == len(right):
                cache[l][r] = len(left) - l
            elif left[l] == right[r]:
                cache[l][r] = edit(l+1, r+1)
            else:
                delete =  1 + edit(l+1, r)
                insert =  1 + edit(l, r+1)
                replace = 1 + edit(l+1, r+1)
                cache[l][r] =  min(delete, insert, replace)
        return cache[l][r]

    cache = []
    for l in range(len(left) + 1):
        cache.append([-1] * (len(right) + 1))
    return edit(0, 0)