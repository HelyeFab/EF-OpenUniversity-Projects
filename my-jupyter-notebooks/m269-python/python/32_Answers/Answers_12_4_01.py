# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 12.4.1 answer

# CELL 1

def maximum(numbers: list) -> int:
    """Return the largest number in numbers.

    Preconditions: numbers is a non-empty list of integers
    """
    if len(numbers) == 1:
        return head(numbers)
    else:
        return max(head(numbers), maximum(tail(numbers)))