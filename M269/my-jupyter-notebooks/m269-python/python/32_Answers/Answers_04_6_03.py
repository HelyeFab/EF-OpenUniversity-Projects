# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 4.6.3 answer

# CELL 1

games_by_row = [
    ['Board game', 'Rating', 'Owned'],
    ['Power Grid',      10 ,   True ],
    [   'Vintage',       8 ,   True ],
    [  'Pandemic',       9 ,  False ]
]

games_by_row[0].append('Price in £')    # add column to header row
games_by_row[1].append(37)              # and every other row
games_by_row[2].append(47)
games_by_row[3].append(26)
games_by_row.insert(1, ['Ticket to Ride', 8, False, 28])   # add row
games_by_row    # display the new table