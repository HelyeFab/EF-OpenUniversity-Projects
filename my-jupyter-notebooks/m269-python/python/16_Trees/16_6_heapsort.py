# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 16.6 Heapsort

### 16.6.1 Binary heap

#### Exercise 16.6.1

### 16.6.2 Inserting items

### 16.6.3 Removing the root

### 16.6.4 Complexity

#### Exercise 16.6.2

#### Exercise 16.6.3

### 16.6.5 Heaps in Python

# CELL 1

from typing import Callable
from algoesup import test
# %run -i ../m269_sorting

from heapq import heappush, heappop

def heapsorted(unsorted: list, key: Callable) -> list:
    """Return a permutation with keys in non-decreasing order.

    Preconditions:
    - all items in unsorted are pairwise comparable
    - for any indices i and j,
      key(unsorted[i]) and key(unsorted[j]) are comparable
    """
    heap = []
    for item in unsorted:
        heappush(heap, (key(item), item) )
    sorted = []
    while len(heap) > 0:
        sorted.append(heappop(heap)[1])
    return sorted

test(heapsorted, sorting_tests)

# CELL 2

from random import shuffle

for doubling in range(5):
    items = list(range(100 * 2**doubling, -1, -1))
    shuffle(items)                              # random sequence
    # %timeit -r 5 heapsorted(items, identity)