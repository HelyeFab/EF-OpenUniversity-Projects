# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 27.4 Undecidability

### 27.4.1 The halting problem

# CELL 1

from typing import Callable

def halts(function: Callable, input: object) -> bool:
    """Return True if and only if function(input) eventually stops."""
    # do some highly sophisticated static analysis here

# CELL 2

def opposite(f: Callable) -> bool:
    """Return True if and only if f(f) doesn't halt.

    Preconditions: f takes a function as argument
    """
    if halts(f, f):     # does f(f) halt?
        while True:
            pass
        return False
    else:
        return True

### 27.4.2 The totality problem

### 27.4.3 Rice's theorem

### 27.4.4 The equivalence problem

### 27.4.5 Reduction and computability

### 27.4.6 The problem landscape

#### Exercise 27.4.1

#### Exercise 27.4.2