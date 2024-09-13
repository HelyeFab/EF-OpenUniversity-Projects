# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 19.1.3 answer

# CELL 1

from algoesup import test
from heapq import heappush, heappop

def winner(strength: list) -> int:
    """Return the index of the winning knight or -1 if no one wins.

    Preconditions: all items in strength are positive integers
    """
    remaining = []  # priority queue of knights still jousting
    for knight in range(len(strength)):
        heappush(remaining, (-strength[knight], knight))

    while len(remaining) > 1:
        # take the two strongest knights
        first = heappop(remaining)
        second = heappop(remaining)
        # if they don't knock each other out
        if first[0] != second[0]:
            # the first (stronger) remains with diminished strength
            heappush(remaining, (first[0] - second[0], first[1]))
    if len(remaining) == 0:
        return -1
    else:
        return remaining[0][1]  # return knight at head of queue

winner_tests = [
    # case,         strength,   winner
    ('no one wins', [5, 3, 6, 2],   -1),
    ('second wins', [5, 3, 6, 1],    1), # winner has initial strength 3
    # your tests
    ('no jousts',   [5],             0),
    ('no knights',  [],             -1),
    # if all knights have the same strength, no one or last one wins
    ('last wins',   [1, 1, 1],       2),    # odd number: last wins
    ('all KO',      [1, 1, 1, 1],   -1)     # even number: all KO
]

test(winner, winner_tests)