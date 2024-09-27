# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 4.7.3 answer

# CELL 1

from algoesup import test

reversed_list_tests = [
    # case,             values,             reversed
    ('empty list',      [],                 []              ),
    ('length 1',        [4],                [4]             ),
    ('length 2',        [5, True],          [True, 5]       ),
    ('length 5',        [5, 6, 7, 8, 9],    [9, 8, 7, 6, 5] ),
    ('same items',      [0, 0, 0],          [0, 0, 0]       )
]

def reversed_list_2(values: list) -> list:
    """Return the same items as values, in inverse order.

    This is a more efficient version of reversed_list.
    Postconditions: the output is
    [values[-1], values [-2], ..., values[1], values[0]]
    """
    reversed = []
    for index in range(len(values)-1, -1, -1):
        reversed.append(values[index])
    return reversed

test(reversed_list_2, reversed_list_tests)