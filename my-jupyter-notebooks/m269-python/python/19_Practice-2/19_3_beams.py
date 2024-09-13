# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 19.3 Beams

### 19.3.1 Exercises

#### Exercise 19.3.1

#### Exercise 19.3.2

#### Exercise 19.3.3

#### Exercise 19.3.4

#### Exercise 19.3.5

# CELL 1

from algoesup import test

def weak_points(beams: set) -> set:
    """Return the points that aren't part of any triangle.

    beams is a set of pairs of integers.
    The output is a set of integers.
    Each integer represents a point.

    Preconditions: for every pair (a, b), a ≠ b
    Postconditions: the output only has points occurring in beams
    """
    pass


weak_points_tests = [
    # case,             beams,                      weak points
    ('no triangle',     {(1,2), (3,1)},             {1, 2, 3}),
    ('missing points',  {(7,3), (3,2)},             {2, 3, 7}),
    # your tests:
]

test(weak_points, weak_points_tests)