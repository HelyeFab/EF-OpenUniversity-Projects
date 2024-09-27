# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 7.3 Queues

### 7.3.1 Queues

#### Exercise 7.3.1

#### Exercise 7.3.2 (optional)

### 7.3.2 Queues with Python lists

# CELL 1

queue = []
queue.append('Alice')   # Alice arrives first
queue.append('Bob')
print('Next person served:', queue.pop(0))
queue.append('Clara')
print('Next person served:', queue.pop(0))
print('Next person served:', queue.pop(0))
print('People still waiting?', len(queue) > 0)

### 7.3.3 Queues with linked lists

# CELL 2

# this code is also in m269_queue.py

class Queue:
    """A last-in, first-out sequence of objects, implemented with a linked list."""

    class Node:
        """A node in a linked list."""

        def __init__(self, item: object):
            """Initialise the node with the given item."""
            self.item = item
            self.next = None

    def __init__(self):
        """Initialise the queue to be empty."""
        self.head = None
        self.last = None
        self.length = 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return self.length

    def front(self) -> object:
        """Return the item at the front of the queue.

        Preconditions: self.size() > 0
        """
        return self.head.item

    def enqueue(self, item) -> None:
        """Add item to the back of the queue."""
        node = Queue.Node(item)
        if self.length == 0:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length = self.length + 1

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        Preconditions: self.size() > 0
        """
        item = self.front()
        self.head = self.head.next
        if self.head == None:
            self.last = None
        self.length = self.length - 1
        return item

# CELL 3

queue = Queue()
queue.enqueue('Alice')   # Alice arrives first
queue.enqueue('Bob')
print('Next person served:', queue.dequeue())
queue.enqueue('Clara')
print('Next person served:', queue.dequeue())
print('Next person served:', queue.dequeue())
print('People still waiting?', queue.size() > 0)

#### Exercise 7.3.3

### 7.3.4 Using queues

#### Exercise 7.3.4

#### Exercise 7.3.5

#### Exercise 7.3.6

# CELL 4

# %run -i ../m269_queue

from algoesup import test

def counting_rhyme(n: int) -> int:
    """Return which child from 1 to n remains last in the circle.

    Preconditions: n > 0
    """
    pass

counting_rhyme_tests = [
    # case,         n,  last child
    ['1 child',     1,          1],
    ['2 children',  2,          1],
    ['3 children',  3,          2]
]

test(counting_rhyme, counting_rhyme_tests)

#### Exercise 7.3.7