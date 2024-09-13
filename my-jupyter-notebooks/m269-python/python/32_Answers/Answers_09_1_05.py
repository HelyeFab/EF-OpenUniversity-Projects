# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 9.1.5 answer

# CELL 1

from algoesup import test

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

def missing_letters(text: str) -> str:
    """Return all English alphabet letters that aren't in text.

    Preconditions: all letters in text are lowercase
    Postconditions: the output are the letters from a to z that
    don't occur in text, in alphabetical order
    """
    occurring = set(text)
    missing = ''
    for letter in LETTERS:
        if letter not in occurring:
            missing = missing + letter
    return missing

PANGRAM = 'the quick brown fox jumps over the lazy dog.'

missing_letters_tests = [
    # case,         text,                           missing
    ['pangram',     PANGRAM,                        ''],
    ['no vowels',   'bcd fgh jklmn pqrst vwxyz',    'aeiou'],
    # new tests:
    ['no text',     '',                             LETTERS],
    ['no a-z',      'Θ(1)',                         LETTERS]
]

test(missing_letters, missing_letters_tests)