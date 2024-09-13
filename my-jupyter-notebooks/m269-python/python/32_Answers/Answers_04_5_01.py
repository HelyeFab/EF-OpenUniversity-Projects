# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 4.5.1 answer

# CELL 1

games_by_column = (                     # each item is a column
    ('Board game', 'Power Grid', 'Vintage', 'Pandemic'),
    ('Rating',              10 ,        8 ,         9 ),
    ('Owned',             True ,     True ,     False )
)

GAME = 0
RATING = 1
OWNED = 2

games_by_column[RATING][3]