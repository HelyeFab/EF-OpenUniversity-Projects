# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 12.5.1 answer

# CELL 1

def positive(numbers: list) -> list:
    """Return a new list of all positive numbers in the input.

    Preconditions: all elements of numbers are integers or floats
    Postconditions:
    the output's elements are in the same order as in the input
    """
    if is_empty(numbers):
        return []
    else:
        solutions = positive(tail(numbers))
        if head(numbers) > 0:
            solutions = prepend(head(numbers), solutions)
        return solutions

positive_tests = [
    # case,             numbers,        positive
    ('shortest input',  [],             []),
    # new tests:
    ('no positives',    [-1, 0, -3],    []),
    ('all positive',    [1, 3],         [1, 3]),
    ('mixed signs',     [3, 0, -1, 2],  [3, 2])
]