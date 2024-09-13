# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 14.5 Merge sort

### 14.5.1 Algorithm

### 14.5.2 Complexity

#### Exercise 14.5.1

### 14.5.3 Code and performance

# CELL 1

from typing import Callable
from algoesup import test

# %run -i ../m269_sorting

def merge(left: list, right: list, key: Callable) -> list:
    """Merge both lists into one with keys in non-decreasing order.

    Preconditions: left and right have keys in non-decreasing order
    """
    left_index = 0
    right_index = 0
    sorted = []
    while left_index < len(left) and right_index < len(right):
        left_item = left[left_index]
        right_item = right[right_index]
        if key(left_item) < key(right_item):
            sorted.append(left_item)
            left_index = left_index + 1
        else:
            sorted.append(right_item)
            right_index = right_index + 1
    for index in range(left_index, len(left)):
        sorted.append(left[index])
    for index in range(right_index, len(right)):
        sorted.append(right[index])
    return sorted

def merge_sorted(unsorted: list, key: Callable) -> list:
    """Return a permutation with keys in non-decreasing order.

    Preconditions: for any indices i and j,
    key(unsorted[i]) and key(unsorted[j]) are comparable
    """
    n = len(unsorted)
    if n < 2:
        return unsorted
    else:
        middle = n // 2
        left_sorted = merge_sorted(unsorted[:middle], key)
        right_sorted = merge_sorted(unsorted[middle:], key)
        return merge(left_sorted, right_sorted, key)

test(merge_sorted, sorting_tests)

# CELL 2

for doubling in range(5):
    items = [0] * 100 * 2**doubling     # 100, 200, 400, ... zeros
    # %timeit -r 5 merge_sorted(items, identity)