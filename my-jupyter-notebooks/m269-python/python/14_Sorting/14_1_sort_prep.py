# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 14.1 Preliminaries

### 14.1.1 Problem

### 14.1.2 Problem instances

# CELL 1

# this code is also in m269_sorting.py

def suit(card: str) -> str:
    """Return the second character of the card.

    Preconditions: card has two characters;
    the first is 'A', '2' to '9', 'T', 'J', 'Q' or 'K'
    the second is 'C', 'D', 'H' or 'S'
    """
    return card[1]

VALUES = 'A23456789TJQK'

def value(card: str) -> int:
    """Return the value of the card.

    Preconditions: as for function 'suit'
    Postconditions: the output is 1 to 13 respectively for
    'A', '2' to '9', 'T', 'J', 'Q', 'K'
    """
    for index in range(len(VALUES)):
        if VALUES[index] == card[0]:
            return index + 1        # return 1—13, not 0—12

def suit_value(card: str) -> tuple:
    """Return a tuple with the suit and value of the card.

    Preconditions: as for function 'suit'
    """
    return (suit(card), value(card))

# CELL 2

suit_value('TD')

# CELL 3

# this code is also in m269_sorting.py

UP_DOWN = ['AS','3H','QD','KC'] # ascending values, descending suits
SAME_VALUE = ['TD', 'TS', 'TH', 'TC']

sorting_tests = [
    # case,        unsorted,           key, sorted
    ('empty list', [],          suit_value, []),
    ('1 card',     ['AS'],      suit_value, ['AS']),
    ('same cards', ['6D','6D'], suit_value, ['6D','6D']),
    ('3 cards',    ['JC','8D','TS'], value, ['8D','TS','JC']),
    ('values up',  UP_DOWN,          value, UP_DOWN),
    ('suits down', UP_DOWN,           suit, ['KC','QD','3H','AS']),
    ('same value', SAME_VALUE,  suit_value, ['TC','TD','TH','TS']),
]

# CELL 4

# this code is also in m269_sorting.py

def identity(item: object) -> object:
    """Return the item, i.e. the key is the whole item."""
    return item

### 14.1.3 Algorithms

### 14.1.4 Sorting in Python

# CELL 5

items = ['2S', 'AS', '2D', 'AD']
items.sort(key=suit_value)
items

# CELL 6

items.sort(suit_value)