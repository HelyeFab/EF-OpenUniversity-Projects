# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 23.2.4 answer

# CELL 1

def lcs_topdown_matrix(left: str, right: str):
    """Return the LCS of both strings using top-down dynamic programming."""

    def lcs(l: int, r: int) -> str:
        """Return the LCS of left[l:] and right[r:].

        Preconditions: 0 ≤ l ≤ len(left) and 0 ≤ r ≤ len(right)
        """
        if cache[l][r] == None:
            if l == len(left) or r == len(right):
                cache[l][r] = ''
            elif left[l] == right[r]:
                cache[l][r] = left[l] + lcs(l + 1, r + 1)
            else:
                skip_left = lcs(l + 1, r)
                skip_right = lcs(l, r + 1)
                if len(skip_left) > len(skip_right):
                    cache[l][r] = skip_left
                else:
                    cache[l][r] = skip_right
            print("cache[", l, "][", r, "] =", "'" + cache[l][r] + "'")
        return cache[l][r]

    cache = []
    for row in range(len(left) + 1):
        cache.append([None] * (len(right) + 1))
    return lcs(0, 0)