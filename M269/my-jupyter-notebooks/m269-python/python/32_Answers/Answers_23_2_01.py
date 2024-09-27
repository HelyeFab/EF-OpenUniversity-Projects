# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 23.2.1 answer

# CELL 1

# %run -i ../m269_rec_list

def lcs(left: str, right: str) -> str:
    """Return the longest common subsequence of both strings."""
    if left == '' or right == '':
        return ''
    elif head(left) == head(right):
        return head(left) + lcs(tail(left), tail(right))
    else:
        skip_right = lcs(left, tail(right))
        skip_left = lcs(tail(left), right)
        if len(skip_left) > len(skip_right):
            return skip_left
        else:
            return skip_right

# CELL 2

lcs('aba', 'baca')