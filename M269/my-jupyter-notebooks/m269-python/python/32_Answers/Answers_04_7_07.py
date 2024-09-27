# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 4.7.7 answer

# CELL 1

def reverse_in_place(values: list) -> None:
    """Reverse the order of the values.

    Postconditions: post-values = [pre-values[len(pre-values) - 1],
        ..., pre-values[1], pre-values[0]]
    """
    left_index = 0
    right_index = len(values) - 1
    while left_index < right_index:
        left_item = values[left_index]
        values[left_index] = values[right_index]
        values[right_index] = left_item
        left_index = left_index + 1
        right_index = right_index - 1

def test_reverse_in_place(test_table: list) -> None:
    """Report which tests for the reverse_in_place function fail."""
    for test_case in test_table:
        name = test_case[0]
        values = test_case[1]
        reversed = test_case[2]
        reverse_in_place(values)
        if values != reversed:
            print(name, 'FAILED:', values, 'instead of', reversed)
    print('Tests finished.')

reversed_list_tests = [
    # case,             values,             reversed
    ('empty list',      [],                 []              ),
    ('length 1',        [4],                [4]             ),
    ('length 2',        [5, True],          [True, 5]       ),
    ('length 5',        [5, 6, 7, 8, 9],    [9, 8, 7, 6, 5] ),
    ('same items',      [0, 0, 0],          [0, 0, 0]       )
]

test_reverse_in_place(reversed_list_tests)