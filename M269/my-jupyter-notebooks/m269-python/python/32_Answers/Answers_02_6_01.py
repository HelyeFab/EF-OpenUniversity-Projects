# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 2.6.1 answer

# CELL 1

def brick_volume(length: int, width: int, height: int) -> int:
    """Return the volume of a brick, given its dimensions.

    Preconditions:
    - length > 0; width > 0; height > 0
    - length, width and height are in millimetres
    Postconditions:
    - the output is length * width * height
    - the output is in cubic millimetres
    """
    return length * width * height