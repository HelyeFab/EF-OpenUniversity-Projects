# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 4.5.2 answer

# CELL 1

tic_tac_toe = (
    ('X', 'O', 'X'),
    (' ', 'X', ' '),
    ('O', ' ', 'O')
)

empty = 0
for row in tic_tac_toe:
    for space in row:
        if space == ' ':
            empty = empty + 1
print(empty)