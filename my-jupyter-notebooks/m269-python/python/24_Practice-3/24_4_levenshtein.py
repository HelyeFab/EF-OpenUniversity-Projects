# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 24.4 Levenshtein distance

# CELL 1

from algoesup import test

edit_tests = [
    # case,                 left,           right,    distance
    ('same word',           'hello',        'hello',        0),
    ('insert',              'rate',         'grate',        1),
    ('delete',              'rate',         'ate',          1),
    ('replace',             'rate',         'fate',         1),
    ('replace',             'algorithm',    'logarithm',    3),
    ('replace & delete',    'yes',          'no',           3),
    ('delete & insert',     'great',        'grate',        2),
    ('replace & insert',    'fast',         'haste',        2),
    ('all three edits',     'GATACA',       'CATCAT',       3),
    # common typo: pressing neighbouring letter on keyboard
    ('replace',             'mimt',         'mint',         1),
    # common typo: pressing neighbouring letters in wrong order
    ('swap letters',        'perquel',      'prequel',      2),
]

### 24.4.1 Exercises

#### Exercise 24.4.1

#### Exercise 24.4.2

# CELL 2

def edit(left: str, right: str) -> int:
    """Return the Levenshtein distance between the strings."""
    pass

test(edit, edit_tests)
# %timeit edit('algorithm', 'logarithm')

#### Exercise 24.4.3

# CELL 3

def edit_indices(left: str, right: str) -> int:
    """Return the Levenshtein distance between the strings."""

    def edit(l: int, r: int) -> int:
        """Return the Levenshtein distance of left[l:] and right[r:].

        Preconditions: 0 ≤ l ≤ len(left) and 0 ≤ r ≤ len(right)
        """
        pass

    pass    # call the inner function and return the result

test(edit_indices, edit_tests)
# %timeit edit_indices('algorithm', 'logarithm')

#### Exercise 24.4.4

#### Exercise 24.4.5

# CELL 4

def edit_topdown(left: str, right: str) -> int:
    """Return the Levenshtein distance between the strings."""

    def edit(l: int, r: int) -> int:
        """Return the Levenshtein distance of left[l:] and right[r:].

        Preconditions: 0 ≤ l ≤ len(left) and 0 ≤ r ≤ len(right)
        """
        pass

    pass

test(edit_topdown, edit_tests)
# %timeit edit_topdown('algorithm', 'logarithm')

#### Exercise 24.4.6

#### Exercise 24.4.7

# CELL 5

def edit_bottomup(left: str, right: str) -> int:
    """Return the Levenshtein distance between the strings."""
    pass

test(edit_bottomup, edit_tests)
# %timeit edit_bottomup('algorithm', 'logarithm')

#### Exercise 24.4.8