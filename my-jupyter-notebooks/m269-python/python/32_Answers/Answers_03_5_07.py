# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 3.5.7 answer

# CELL 1

def maximum(left: float, right: float) -> float:
    """Return the largest of the two values.

    Postconditions:
    return left if left > right, otherwise return right
    """
    if left > right:
        largest = left
    else:
        largest = right
    return largest

# CELL 2

maximum(5, 3.5) == 5

# CELL 3

maximum(-5.3, 3.5) == 3.5

# CELL 4

maximum(-3, -3) == -3