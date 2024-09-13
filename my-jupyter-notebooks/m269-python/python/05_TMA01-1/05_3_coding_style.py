# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 5.3 Coding style

### 5.3.1 The Zen of Python

# CELL 1

import this

### 5.3.2 Linters

# CELL 2

# %load_ext algoesup.magics
# %ruff on

# CELL 3

def length(list):
    l = 0
    for value in list:
        l = l + 1

# CELL 4

import platform  # allowed

if platform.system() in ('Linux', 'Darwin'):
    # %allowed on --config m269-24j --unit 5 --method
else:
    # %allowed on --config m269-24j --unit 5

# CELL 5

from math import sqrt

def some_function(n: int) -> int:
    """To be implemented."""
    arabic_to_roman = {1: "I", 5: "V"}
    numbers = [1, 2, 1, 0]
    numbers.count(1)
    pass