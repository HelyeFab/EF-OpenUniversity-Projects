# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 14.8 Pigeonhole sort

### 14.8.1 Comparison sort complexity

### 14.8.2 Algorithm

### 14.8.3 Complexity

### 14.8.4 Code and tests

# CELL 1

from typing import Callable

def pigeonhole_sorted(unsorted: list, key: Callable, slots: int) -> list:
    """Return a permutation with keys in non-decreasing order.

    Precondition: for each item in unsorted 0 <= key(item) < slots
    """
    pigeonholes = []
    for slot in range(slots):
        pigeonholes.append([])
    for item in unsorted:
        pigeonholes[key(item)].append(item)
    sorted = []
    for slot in pigeonholes:
        for item in slot:
            sorted.append(item)
    return sorted

# CELL 2

from algoesup import test

# %run -i ../m269_sorting

def value_nat(card: str) -> int:
    """Return 0 to 12 for value A2...9TJQK respectively.

    Preconditions: as for function 'suit'
    """
    return value(card) - 1  # the value function returns 1 to 13

def suit_nat(card: str) -> int:
    """Return 0 to 3 for suit 'C', 'D', 'H' and 'S' respectively.

    Preconditions: as for function 'suit'
    """
    return {'C':0, 'D':1, 'H':2, 'S':3}[card[1]]

def card_nat(card: str) -> int:
    """Return 0 to 51 according to the sorted order of the card.

    Cards are sorted first by suit, then by value.
    Preconditions: as for function 'suit'
    """
    return suit_nat(card) * 13 + value_nat(card)

pigeonhole_sorted_tests = [
    # case,       unsorted,          key,    slots, sorted
    ('no cards',   [],               card_nat,  52, []),
    ('1 card',     ['AS'],           card_nat,  52, ['AS']),
    ('same card',  ['6D','6D'],      card_nat,  52, ['6D','6D']),
    ('3 cards',    ['JC','8D','TS'], value_nat, 13, ['8D','TS','JC']),
    ('value up',   UP_DOWN,          value_nat, 13, UP_DOWN),
    ('suit down',  UP_DOWN,          suit_nat,   4, ['KC','QD','3H','AS']),
    ('same value', SAME_VALUE,       card_nat,  52, ['TC','TD','TH','TS']),
]

test(pigeonhole_sorted, pigeonhole_sorted_tests)

### 14.8.5 Performance

# CELL 3

for doubling in range(5):
    items = list(range(100 * 2**doubling))
    # %timeit -r 5 pigeonhole_sorted(items, identity, len(items))