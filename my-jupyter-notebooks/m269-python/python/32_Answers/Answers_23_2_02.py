# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 23.2.2 answer

# CELL 1

# %run -i ../m269_rec_list

def lcs_topdown(left: str, right: str) -> str:
    """Return the LCS of both strings using top-down dynamic programming."""

    def lcs(left: str, right: str) -> str:
        """Auxiliary recursive function."""
        if (left, right) not in cache:
            if left == '' or right == '':
                cache[(left, right)] = ''
            elif head(left) == head(right):
                cache[(left, right)] = head(left) + lcs(tail(left), tail(right))
            else:
                skip_right = lcs(left, tail(right))
                skip_left = lcs(tail(left), right)
                if len(skip_left) > len(skip_right):
                    cache[(left, right)] = skip_left
                else:
                    cache[(left, right)] = skip_right
            # print() doesn't show quote marks, so add them
            print("cache[(", "'" + left + "'", ",", "'" + right + "'", ")] =",
                  "'" + cache[(left, right)] + "'")
        return cache[(left, right)]

    cache = dict()
    return lcs(left, right)