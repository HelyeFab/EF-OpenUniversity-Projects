# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 14.6 Quicksort

### 14.6.1 Algorithm

### 14.6.2 Complexity

#### Exercise 14.6.1

### 14.6.3 Code and performance

# CELL 1

from typing import Callable
from algoesup import test

# %run -i ../m269_sorting

def quick_sorted(unsorted: list, key: Callable) -> list:
    """Return a permutation with keys in non-decreasing order.

    Preconditions: for any indices i and j,
    key(unsorted[i]) and key(unsorted[j]) are comparable
    """
    # base case: sequences with 0 or 1 items are sorted
    if len(unsorted) < 2:
        return unsorted
    else:
        # divide the input: select the pivot and create the partitions
        smaller = []
        larger = []
        pivot = unsorted[0]
        pivot_key = key(pivot)
        for index in range(1, len(unsorted)):
            item = unsorted[index]
            if key(item) < pivot_key:
                smaller.append(item)
            else:
                larger.append(item)
        # recur into the partitions and combine the results
        return quick_sorted(smaller, key) + [pivot] + quick_sorted(larger, key)

test(quick_sorted, sorting_tests)

# CELL 2

for doubling in range(5):
    items = list(range(100 * 2**doubling))
    # %timeit -r 5 quick_sorted(items, identity)

# CELL 3

from random import shuffle

for doubling in range(5):
    items = list(range(100 * 2**doubling))
    shuffle(items)
    # %timeit -r 5 quick_sorted(items, identity)

### 14.6.4 In-place version