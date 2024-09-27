# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 27.1.2 answer

# CELL 1

from algoesup import test
# %run -i ../m269_tm

is_valid = {
    ('start', 'a'):     ('a', RIGHT, 'letter'),
    ('start', '0'):     ('0', RIGHT, 'digit'),
    ('start', None):    (False, STAY, 'start'),

    ('letter', 'a'):    ('a', RIGHT, 'letter'),
    ('letter', '0'):    ('0', RIGHT, 'both'),
    ('letter', None):   (False, STAY, 'letter'),

    ('digit', 'a'):     ('a', RIGHT, 'both'),
    ('digit', '0'):     ('0', RIGHT, 'digit'),
    ('digit', None):    (False, STAY, 'digit'),

    ('both', 'a'):      ('a', RIGHT, 'both'),
    ('both', '0'):      ('0', RIGHT, 'both'),
    ('both', None):     (True, STAY, 'both'),
}

check_TM(is_valid)