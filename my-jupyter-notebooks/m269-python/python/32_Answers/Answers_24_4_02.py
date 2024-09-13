# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 24.4.2 answer

# CELL 1

def edit(left: str, right: str) -> int:
    """Return the Levenshtein distance between the strings."""
    if left == '':
        return len(right)
    elif right == '':
        return len(left)
    elif left[0] == right[0]:
        return edit(left[1:], right[1:])
    else:
        delete =  1 + edit(left[1:], right)     # delete left head
        insert =  1 + edit(left, right[1:])     # insert right head
        replace = 1 + edit(left[1:], right[1:])
        return min(delete, insert, replace)