# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 9.2.5 answer

# CELL 1

from algoesup import test

def winner(votes: list) -> str:
    results = dict()    # map candidate (str) to their votes (int)
    for candidate in votes:
        if candidate in results:
            results[candidate] = results[candidate] + 1
        else:
            results[candidate] = 1
    winner_votes = 0
    for (candidate_name, candidate_votes) in results.items():
        if candidate_votes > winner_votes:
            winner_votes = candidate_votes
            winner_name = candidate_name
        elif candidate_votes == winner_votes:
            winner_name = 'round 2'
    return winner_name

winner_tests = [
    # case,         votes,                              name
    ['2 of 2 tied', ['Alice', 'Bob', 'Bob', 'Alice'],   'round 2'],
    ['1 of 2 wins', ['Alice', 'Bob', 'Alice', 'Alice'], 'Alice'  ],
    ['1 of 3 wins', ['Bob', 'Chan', 'Chan', 'Alice'],   'Chan'   ],
    # new tests:
    ['1 vote',      ['Chan'],                           'Chan'   ],
    ['1 vote per candidate', ['Bob', 'Chan', 'Alice'],  'round 2'],
    ['1 candidate', ['Bob'] * 5,                        'Bob'    ],
    ['2 of 3 tied', ['Al', 'Bob', 'Chan', 'Al', 'Bob'], 'round 2']
]

test(winner, winner_tests)