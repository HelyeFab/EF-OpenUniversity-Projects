# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 27.2 The Church–Turing thesis

### 27.2.1 Computational models

### 27.2.2 Universal models

### 27.2.3 Length of string

# CELL 1

# %run -i ../m269_tm
from algoesup import test

length = {
    # (state, symbol):  (symbol, head, state)
    # if 'a', mark the position and start incrementing counter
    ('start', 'a'):     ('X', RIGHT, 'up'),
    # if empty string, write 0 and stop
    ('start', None):    (0, STAY, 'start'),

    # before incrementing, skip all letters
    ('up', 'a'):        ('a', RIGHT, 'up'),
    # if bit is zero: increment and return to marked position
    ('up', 0):          (1, LEFT, 'back'),
    # if bit is one, carry over: keep incrementing
    ('up', 1):          (0, RIGHT, 'up'),
    # end of binary number: increment and go back
    ('up', None):       (1, LEFT, 'back'),

    # to return to marked position, skip all digits and letters
    ('back', 0):        (0, LEFT, 'back'),
    ('back', 1):        (1, LEFT, 'back'),
    ('back', 'a'):      ('a', LEFT, 'back'),
    # restore marked position to 'a'; start again with next letter
    ('back', 'X'):      ('a', RIGHT, 'start')
}

length_tests = [
    # case,     TM,     input,              debug, output
    ('empty',   length, [None],             False, [0]),
    ('one',     length, ['a'],              False, [1]),
    ('two',     length, ['a', 'a'],         False, [0, 1]),
    ('three',   length, ['a', 'a', 'a'],    False, [1, 1]),
]

test(run_TM, length_tests)

#### Exercise 27.2.1

#### Exercise 27.2.2