# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 19.5 A knight goes places

### 19.5.1 Exercises

#### Exercise 19.5.1

#### Exercise 19.5.2

#### Exercise 19.5.3

#### Exercise 19.5.4

# CELL 1

from algoesup import test

def knight_moves(size: tuple, start: tuple, end: tuple) -> int:
    """Return least number of knight moves from start to end.

    Return -1 if end is not reachable from start.

    Preconditions:
    - size is a pair (rows, columns) with rows > 0 and columns > 0
    - start and end are pairs (r, c) with 0 <= r < rows and 0 <= c < columns
    """
    pass

knight_moves_tests = [
    # case,             size,   start,  end,    moves
    ('1x1 board',       (1, 1), (0, 0), (0, 0),     0),
    ('1 row, 2 cols',   (1, 2), (0, 0), (0, 1),    -1),
    ('2 rows, 1 col',   (2, 1), (1, 0), (0, 0),    -1),
    ('start = end',     (3, 3), (1, 1), (1, 1),     0),
    ('bottom left',     (5, 6), (3, 4), (4, 0),     3), # figure 19.5.1
    ('bottom right',    (5, 6), (3, 4), (4, 5),     4), # figure 19.5.1
    ('3x3 to centre',   (3, 3), (0, 0), (1, 1),    -1), # figure 19.5.2
]

test(knight_moves, knight_moves_tests)