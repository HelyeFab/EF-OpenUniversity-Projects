# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 6.6 Using dynamic arrays

### 6.6.1 The `ArraySequence` class

# CELL 1

# %run -i ../m269_array
# %run -i ../m269_sequence

# CELL 2

# this code is also in m269_sequence.py

import math

class ArraySequence(Sequence):
    """A dynamic array implementation of the sequence ADT."""

    def __init__(self):
        """Create an empty sequence."""
        self.items = DynamicArray(1)
        self.size = 0

    def capacity(self) -> float:
        return math.inf     # infinite capacity

    def length(self) -> int:
        return self.size

    def get_item(self, index: int) -> object:
        return self.items.get_item(index)

    def set_item(self, index: int, item: object) -> None:
        self.items.set_item(index, item)

    def insert(self, index: int, item: object) -> None:
        if self.size == self.items.length():    # array full
            self.items.resize(2 * self.size)    # double the capacity

        for position in range(self.size - 1, index - 1, -1):
            self.items.set_item(position + 1, self.items.get_item(position))
        self.items.set_item(index, item)
        self.size = self.size + 1

# CELL 3

sequence = ArraySequence()
print('array', sequence.items, 'stores sequence', sequence)
for value in range(0, 5):
    sequence.append(value)
    print('array', sequence.items, 'stores sequence', sequence)

# CELL 4

# %run -i ../m269_test

test_init(ArraySequence())
for length in range(10):
    print('Testing length', length)
    test_append(ArraySequence(), length)
    test_insert_start(ArraySequence(), length)
    test_set_item(ArraySequence(), length)

#### Exercise 6.6.1 (optional)

# CELL 5

# %run -i ../m269_test

for length in range(5):
    print('Testing length', length)
    test_remove(ArraySequence(), length)