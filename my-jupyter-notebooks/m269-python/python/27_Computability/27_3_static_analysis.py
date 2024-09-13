# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 27.3 Static analysis

### 27.3.1 Functions on functions

# CELL 1

help(len)

# CELL 2

# %run -i ../m269_sorting        # defines key functions for sorting

sorted(['2S', 'AS', '2D', 'AD'], key=suit)  # diamonds, then spades

# CELL 3

sorted(['2S', 'AS', '2D', 'AD'], key=value) # aces, then twos

# CELL 4

help(suit)      # replace suit with value to see what value does

# CELL 5

from inspect import getsource

print(getsource(suit))  # replace suit with value if you wish

### 27.3.2 Writing functions on functions

# CELL 6

from typing import Callable

def insertion_sort(items: list, key: Callable) -> None:
    for first_unsorted in range(1, len(items)):
        to_sort = items[first_unsorted]
        the_key = key(to_sort)
        index = first_unsorted
        while index > 0 and key(items[index - 1]) > the_key:
            items[index] = items[index - 1]
            index = index - 1
        items[index] = to_sort

### 27.3.3 Navel gazing

# CELL 7

help(help)

# CELL 8

def has_loop(function: Callable) -> bool:
    """Check if the code of `function` includes 'while' or 'for' and 'in'."""
    text = getsource(function)
    return ' while ' in text or (' for ' in text and ' in ' in text)

# CELL 9

has_loop(insertion_sort)

# CELL 10

has_loop(suit)  # replace suit with value if you wish

# CELL 11

has_loop(has_loop)

#### Exercise 27.3.1 (optional)