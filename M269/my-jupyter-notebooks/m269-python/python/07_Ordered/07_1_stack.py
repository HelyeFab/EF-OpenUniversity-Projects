# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 7.1 Stacks

### 7.1.1 The stack ADT

#### Exercise 7.1.1

#### Exercise 7.1.2

### 7.1.2 Implementing with an array

# CELL 1

numbers = []    # stack
for number in range(3):
    print('push', number)
    numbers.append(number)
while len(numbers) > 0:
    print('pop', numbers[-1])
    numbers.pop(-1)

# CELL 2

# this code is also in m269_stack.py

class Stack:
    "A last-in, first-out sequence of objects, implemented with a Python list."""

    def __init__(self):
        """Initialise the stack to be empty."""
        self.items = []

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

    def peek(self) -> object:
        """Return the top item in the stack.

        Preconditions: self.size() > 0
        """
        return self.items[-1]

    def pop(self) -> object:
        """Remove and return the top item from the stack.

        Preconditions: self.size() > 0
        """
        return self.items.pop(-1)

    def push(self, item: object) -> None:
        """Put the given item on top of the stack.

        Postconditions: post-self.peek() == item
        """
        self.items.append(item)

# CELL 3

numbers = Stack()
for number in range(3):
    print('push', number)
    numbers.push(number)
while numbers.size() > 0:
    print('pop', numbers.peek())
    numbers.pop()

### 7.1.3 Implementing with a linked list

# CELL 4

# this code is also in m269_stack.py

class LinkedListStack:
    """A last-in, first-out sequence of objects, implemented with a linked list."""

    class Node:
        """A node in a linked list."""

        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the stack to be empty."""
        self.head = None
        self.length = 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return self.length

    def peek(self) -> object:
        """Return the top item in the stack.

        Preconditions: self.size() > 0
        """
        return self.head.item

    def pop(self) -> object:
        """Remove and return the top item from the stack.

        Preconditions: self.length() > 0
        """
        item = self.head.item
        self.head = self.head.next
        self.length = self.length - 1
        return item

    def push(self, item: object) -> None:
        """Put the given item on top of the stack.

        Postconditions: post-self.peek() == item
        """
        node = LinkedListStack.Node(item)
        node.next = self.head
        self.head = node
        self.length = self.length + 1

# CELL 5

numbers = LinkedListStack()
for number in range(3):
    print('push', number)
    numbers.push(number)
while numbers.size() > 0:
    print('pop', numbers.peek())
    numbers.pop()

#### Exercise 7.1.3