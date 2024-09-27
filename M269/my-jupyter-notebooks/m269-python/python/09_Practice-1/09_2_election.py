# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 9.2 Election

# CELL 1

from algoesup import test

def winner(votes: list) -> str:
    """Return the most frequent string in votes, a list of strings.

    Preconditions:
    - votes isn't empty and doesn't have the string 'round 2'
    Postconditions:
    - return 'round 2' if two or more strings are equally frequent
    """
    pass

winner_tests = [
    # case,         votes,                              name
    ['2 of 2 tied', ['Alice', 'Bob', 'Bob', 'Alice'],   'round 2'],
    ['1 of 2 wins', ['Alice', 'Bob', 'Alice', 'Alice'], 'Alice'  ],
    ['1 of 3 wins', ['Bob', 'Chan', 'Chan', 'Alice'],   'Chan'   ],
    # new tests:
]

test(winner, winner_tests)

### 9.2.1 Problem definition

#### Exercise 9.2.1

### 9.2.2 Algorithm and complexity

#### Exercise 9.2.2

#### Exercise 9.2.3

#### Exercise 9.2.4

### 9.2.3 Code and tests

#### Exercise 9.2.5