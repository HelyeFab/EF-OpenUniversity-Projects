# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 23.2.3 answer

# CELL 1

def lcs_indices(left: str, right: str):
    """Return the LCS of left and right using indices, not slicing."""

    def lcs(l: int, r: int) -> str:
        """Return the LCS of left[l:] and right[r:].

        Preconditions: 0 ≤ l ≤ len(left) and 0 ≤ r ≤ len(right)
        """
        if l == len(left) or r == len(right):
            return ''
        elif left[l] == right[r]:
            return left[l] + lcs(l + 1, r + 1)
        else:
            skip_right = lcs(l, r + 1)
            skip_left = lcs(l + 1, r)
            if len(skip_left) > len(skip_right):
                return skip_left
            else:
                return skip_right

    return lcs(0, 0)