# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 12.3 Length of a sequence

### 12.3.1 Recursive definition

#### Exercise 12.3.1

### 12.3.2 Code

# CELL 1

# this code is also in m269_rec_list.py

def head(items: list) -> object:
    """Return the first item of the list.

    Preconditions: items isn't empty
    """
    return items[0]

def tail(items: list) -> list:
    """Return the list without the first item.

    Preconditions: items isn't empty
    """
    return items[1:]

def is_empty(items: list) -> bool:
    """Return True if and only if the list is empty."""
    return items == []

# CELL 2

def length(items: list) -> int:
    """Return the number of objects in the list."""
    if is_empty(items):
        return 0
    else:
        return length(tail(items)) + 1

# CELL 3

length([])

# CELL 4

length(['one', 'two', 'three'])

### 12.3.3 Mistakes

# CELL 5

def wrong_length(items: list) -> int:
    return wrong_length(tail(items)) + 1

# CELL 6

tail([])

# CELL 7

wrong_length([1, 2, 3])