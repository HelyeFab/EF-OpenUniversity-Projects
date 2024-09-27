# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 14.3 Insertion sort

### 14.3.1 Recursive version

### 14.3.2 Iterative version

# CELL 1

from typing import Callable

def insertion_sort(items: list, key: Callable) -> None:
    """Sort the items in-place, with keys in non-decreasing order.

    Preconditions: for any indices i and j,
    key(items[i]) and key(items[j]) are comparable
    """
    # go through all items in the unsorted part
    for first_unsorted in range(1, len(items)):
        to_sort = items[first_unsorted]
        # apply the key function given as input
        the_key = key(to_sort)
        # to start, index where to put item is index where it is now
        index = first_unsorted
        # for each sorted item larger than the one to sort
        while index > 0 and key(items[index - 1]) > the_key:
            # copy it to the right, i.e. one position up
            items[index] = items[index - 1]
            # and proceed with the next sorted item on the left
            index = index - 1
        # sorted item on the left isn't larger: we found the index
        items[index] = to_sort      # put the unsorted item there

# CELL 2

from algoesup import test

# %run -i ../m269_sorting

def insertion_sorted(unsorted: list, key: Callable) -> list:
    """Return a permutation with keys in non-decreasing order.

    Preconditions: for any indices i and j,
    key(unsorted[i]) and key(unsorted[j]) are comparable
    """
    items = list(unsorted)     # make a copy
    insertion_sort(items, key)
    return items

test(insertion_sorted, sorting_tests)

### 14.3.3 Complexity

### 14.3.4 Performance

# CELL 3

# %run -i ../m269_sorting

for doubling in range(5):
    # generate lists of length 100, 200, 400, 800, 1600
    # each list has the integers from 0 to length - 1
    items = list(range(100 * 2**doubling))
    # %timeit -r 5 insertion_sorted(items, identity)

# CELL 4

for doubling in range(5):
    items = list(range(100 * 2**doubling, -1, -1))
    # %timeit -r 5 insertion_sorted(items, identity)

#### Exercise 14.3.1