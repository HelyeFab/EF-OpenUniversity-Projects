# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 12.4.3 answer

# CELL 1

from algoesup import test

# %run -i ../m269_rec_list

def value(items: list, index: int) -> object:
    """Return the value at position index of items.

    Preconditions: 0 <= index < len(items)
    """
    if index == 0:
        return head(items)
    else:
        return value(tail(items), index - 1)

value_tests = [
    # case,             items,      index,  value
    ('shortest input',  [5],        0,      5),
    ('access last',     [3, 4, 1],  2,      1),
    ('access middle',   [3, 4, 1],  1,      4)
]