# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 6.2 Static arrays

### 6.2.1 Variables and assignments

# CELL 1

x = 1           # the x-y coordinates of a 2D point
y = 2
pair = [x, y]
point = pair

# CELL 2

y = 3

# CELL 3

point

# CELL 4

pair[1] = 3

# CELL 5

point

### 6.2.2 The `StaticArray` class

# CELL 6

# this code is also in m269_array.py

class StaticArray:
    """A fixed-length sequence of references in contiguous memory."""

    def __init__(self, length: int):
        """Create an array of the given length.

        Preconditions: length >= 0
        Postconditions: every item in the array is None
        """
        # assume lists are stored in arrays
        self.items = [None] * length

    def length(self) -> int:
        """Return the length of the array."""
        return len(self.items)

    def get_item(self, index: int) -> object:
        """Return the item at the given index.

        Preconditions: 0 <= index < self.length()
        """
        return self.items[index]

    def set_item(self, index: int, item: object) -> None:
        """Replace the item at the given index with the given item.

        Preconditions: 0 <= index < self.length()
        Postconditions: self.get_item(index) == item
        """
        self.items[index] = item

    def __str__(self) -> str:
        """Return a string representation of the array."""
        return str(self.items)

### 6.2.3 Testing methods

# CELL 7

# this code is also in m269_test.py

def check(case: str, actual: object, expected: object, context: object) -> None:
    """Write a message if actual and expected are different."""
    if actual != expected:
        print(case, 'FAILED for', context, ':', actual, 'instead of', expected)

# CELL 8

def test_init(length: int) -> None:
    """Create a new array of the given length and check it.

    Preconditions: length >= 0
    """
    array = StaticArray(length)
    check('length', array.length(), length, array)
    for index in range(0, length):
        check('initial item', array.get_item(index), None, array)

# CELL 9

def test_set_item(length: int) -> None:
    """Create an array of the given length, replace all items and check it.

    Preconditions: length >= 0
    """
    array = StaticArray(length)
    for index in range(length):
        array.set_item(index, index)
    for index in range(length):
        check('replaced item', array.get_item(index), index, array)

# CELL 10

test_init(0)    # edge case: length zero
for length in range(1, 11):
    test_init(length)
    test_set_item(length)