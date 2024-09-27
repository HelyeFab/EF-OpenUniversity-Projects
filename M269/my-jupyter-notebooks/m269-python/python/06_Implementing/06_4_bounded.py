# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 6.4 Bounded sequences

### 6.4.1 Outlining algorithms

### 6.4.2 Insertion

### 6.4.3 The `BoundedSequence` class

# CELL 1

# %run -i ../m269_array
# %run -i ../m269_sequence

class BoundedSequence(Sequence):
    """A sequence with a fixed capacity."""

    def __init__(self, capacity: int):
        """Create an empty sequence that can hold 'capacity' items.

        Preconditions: capacity >= 0
        """
        self.items = StaticArray(capacity)
        self.size = 0

    def capacity(self) -> int:
        return self.items.length()

    def length(self) -> int:
        return self.size

    def get_item(self, index: int) -> object:
        return self.items.get_item(index)

    def set_item(self, index: int, item: object) -> None:
        self.items.set_item(index, item)

    def insert(self, index: int, item: object) -> None:
        for position in range(self.size - 1, index, -1):
            self.items.set_item(position + 1, self.items.get_item(position))
        self.items.set_item(index, item)
        self.size = self.size + 1

# CELL 2

items = BoundedSequence(5)
print(items)
for item in ('ready', 'set', 'go!'):
    items.append(item)
    print(items)
print('Can have', items.capacity() - items.length(), 'more items.')

# CELL 3

# %run -i ../m269_test

for capacity in range(4):
    print('Testing capacity', capacity)
    test_init(BoundedSequence(capacity))
    for length in range(capacity + 1):
        print('Testing length', length)
        test_append(BoundedSequence(capacity), length)
        test_insert_start(BoundedSequence(capacity), length)
        test_set_item(BoundedSequence(capacity), length)

#### Exercise 6.4.1

#### Exercise 6.4.2

#### Exercise 6.4.3 (optional)

# CELL 4

for capacity in range(4):
    print('Testing capacity', capacity)
    for length in range(capacity + 1):
        print('Testing length', length)
        test_remove(BoundedSequence(capacity), length)