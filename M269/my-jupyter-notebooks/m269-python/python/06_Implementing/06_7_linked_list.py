# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 6.7 Linked lists

### 6.7.1 Traversing a linked list

### 6.7.2 Inserting an item

#### Exercise 6.7.1

### 6.7.3 The `LinkedSequence` class

# CELL 1

node = None
node.next

# CELL 2

# %run -i ../m269_sequence

import math

class LinkedSequence(Sequence):
    """A linked list implementation of the sequence ADT."""

    class Node:
        """A node in a linked list."""

        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the sequence to be empty."""
        self.head = None

    def capacity(self) -> float:
        return math.inf     # infinite capacity

    def length(self) -> int:
        size = 0
        current = self.head
        while current != None:
            size = size + 1
            current = current.next
        return size

    def get_item(self, index: int) -> object:
        current = self.head
        for times in range(index):
            current = current.next
        return current.item

    def set_item(self, index: int, item: object) -> None:
        current = self.head
        for times in range(index):
            current = current.next
        current.item = item

    def insert(self, index: int, item: object) -> None:
        new = LinkedSequence.Node(item)
        if index == 0:
            new.next = self.head
            self.head = new
        else:
            before = self.head
            for times in range(index - 1):
                before = before.next
            new.next = before.next
            before.next = new

# CELL 3

# %run -i ../m269_test

test_init(LinkedSequence())
for length in range(10):
    print('Testing length', length)
    test_append(LinkedSequence(), length)
    test_insert_start(LinkedSequence(), length)
    test_set_item(LinkedSequence(), length)

#### Exercise 6.7.2 (optional)

# CELL 4

for length in range(5):
    print('Testing length', length)
    test_remove(LinkedSequence(), length)

### 6.7.4 Linked list v. array

#### Exercise 6.7.3