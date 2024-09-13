# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 14.4 Selection sort

### 14.4.1 Recursive version

### 14.4.2 Iterative version

#### Exercise 14.4.1

### 14.4.3 Code

# CELL 1

from typing import Callable

def selection_sort(items: list, key: Callable) -> None:
    """Sort the items in-place, with keys in non-decreasing order.

    Preconditions: for any indices i and j,
    key(items[i]) and key(items[j]) are comparable
    """
    for first_unsorted in range(0, len(items)-1):
        smallest = first_unsorted
        for index in range(smallest+1, len(items)):
            if key(items[index]) < key(items[smallest]):
                smallest = index
        unsorted_item = items[first_unsorted]
        items[first_unsorted] = items[smallest]
        items[smallest] = unsorted_item

# CELL 2

from algoesup import test

# %run -i ../m269_sorting

def selection_sorted(unsorted: list, key: Callable) -> list:
    """Return a permutation with keys in non-decreasing order.

    Preconditions: for any indices i and j,
    key(unsorted[i]) and key(unsorted[j]) are comparable
    """
    sorted = list(unsorted)     # make a copy
    selection_sort(sorted, key)
    return sorted

test(selection_sorted, sorting_tests)

# CELL 3

for doubling in range(5):
    items = list(range(100 * 2**doubling))          # sorted order
    # %timeit -r 5 selection_sorted(items, identity)

# CELL 4

for doubling in range(5):
    items = list(range(100 * 2**doubling, -1, -1))  # reverse order
    # %timeit -r 5 selection_sorted(items, identity)

### 14.4.4 Select largest

#### Exercise 14.4.2