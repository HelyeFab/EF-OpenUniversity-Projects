# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 2.6 Functions in Python

# CELL 1

import math

def circumference(radius: float) -> float:
    """Return the length of the circumference for the given radius.

    Preconditions: radius > 0
    Postconditions: the output is 2 * π * radius
    """
    length = 2 * math.pi * radius
    return length

# CELL 2

circumference(1) # calculate for radius = 1

# CELL 3

def circumference(radius: float) -> float:
    """Return the length of the circumference for the given radius.

    Preconditions: radius > 0
    Postconditions: the output is 2 * π * radius
    """
    return 2 * math.pi * radius

### 2.6.1 Documentation

# CELL 4

help(circumference)

# CELL 5

help(max)

### 2.6.2 Mistakes

# CELL 6

return = 2 * math.pi * radius

# CELL 7

diameter = 2 * radius

# CELL 8

"""This is a docstring."""              # note the syntax colouring

# CELL 9

''''''This is not a docstring.''''''    # different syntax colouring

# CELL 10

def circumference(radius: float) -> float:
"""Return bla bla bla ...
"""
    return 2 * math.pi * diameter

# CELL 11

def circumference(radius: float) -> float:
    """Return bla bla bla ...
    """
return 2 * math.pi * diameter

# CELL 12

circumference(1)

# CELL 13

def circumference(radius: float) -> float:
    """Return ..."""
    diameter = 2 * radius
    length = math.pi * diameter

#### Exercise 2.6.1

# CELL 14

def brick_volume(length: int):
    """Return ...
    """

# CELL 15

# brick_volume(2, 3, 4)   # the output should be 2 * 3 * 4 = 24

#### Exercise 2.6.2

# CELL 16

# replace this by a function definition

# replace this by a function call