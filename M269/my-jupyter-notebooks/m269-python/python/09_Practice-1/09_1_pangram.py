# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 9.1 Pangram

# CELL 1

from algoesup import test

def missing_letters(text: str) -> str:
    """Return all English alphabet letters that aren't in text.

    Preconditions: all letters in text are lowercase
    Postconditions: the output are the letters from a to z that
    don't occur in text, in alphabetical order
    """
    pass

PANGRAM = 'the quick brown fox jumps over the lazy dog.'

missing_letters_tests = [
    # case,         text,                           missing
    ['pangram',     PANGRAM,                        ''],
    ['no vowels',   'bcd fgh jklmn pqrst vwxyz',    'aeiou'],
    # new tests:
]

test(missing_letters, missing_letters_tests)

### 9.1.1 Problem definition

#### Exercise 9.1.1

### 9.1.2 Algorithm and complexity

#### Exercise 9.1.2

#### Exercise 9.1.3

#### Exercise 9.1.4

### 9.1.3 Code and tests

#### Exercise 9.1.5

#### Exercise 9.1.6 (optional)