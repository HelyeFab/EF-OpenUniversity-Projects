# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 19.1 Jousting

### 19.1.1 Exercises

#### Exercise 19.1.1

#### Exercise 19.1.2

#### Exercise 19.1.3

# CELL 1

from algoesup import test

def winner(strength: list) -> int:
    """Return the index of the winning knight or -1 if no one wins.

    Preconditions: all items in strength are positive integers
    """
    pass

winner_tests = [
    # case,         strength,   winner
    ('no one wins', [5, 3, 6, 2],   -1),
    ('second wins', [5, 3, 6, 1],    1), # winner has initial strength 3
    # your tests
]

test(winner, winner_tests)