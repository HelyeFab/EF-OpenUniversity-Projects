# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 7.4 Priority queues

### 7.4.1 With dynamic arrays: version 1

#### Exercise 7.4.1

# CELL 1

tasks = []  # a priority queue
tasks.append( ('go on holiday', 2) )
tasks.sort()
tasks.append( ('finish this chapter', 3) )
tasks.sort()
tasks.append( ('answer email', 1) )
tasks.sort()
for times in range(len(tasks)):
    print(tasks[-1][1], tasks[-1][0])  # print priority and task
    tasks.pop(-1)

# CELL 2

tasks = []  # a priority queue
tasks.append( (2, 'go on holiday') )
tasks.append( (1, 'answer email') )
tasks.append( (3, 'finish this chapter') )
tasks.append( (1, 'remove old files') )
tasks.sort()
while tasks != []:
    task = tasks.pop(-1)
    print(task[0], task[1])

### 7.4.2 With dynamic arrays: version 2

# CELL 3

# this code is also in m269_priority.py

class ArrayPriorityQueue:

    """A dynamic array implementation of a fair max-priority queue.

    Items with the same priority are retrieved in FIFO order.
    """

    def __init__(self):
        """Create a new empty priority queue."""
        self.priorities = []    # in ascending order
        self.items = []

    def length(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)

    def find_max(self) -> object:
        """Return the oldest item with the highest priority.

        Preconditions: self.length() > 0
        """
        return self.items[-1]

    def remove_max(self) -> None:
        """Remove the oldest item with the highest priority.

        Preconditions: self.length() > 0
        """
        self.items.pop(-1)
        self.priorities.pop(-1)

    def insert(self, item: object, priority: object) -> None:
        """Add item with the given priority to the queue.

        Preconditions:
        - priority is comparable to the priorities of all existing items
        """
        index = 0
        # compute the index where to insert the item
        self.items.insert(index, item)
        self.priorities.insert(index, priority)

#### Exercise 7.4.2

#### Exercise 7.4.3

# CELL 4

# %run -i ../m269_test

hospital = ArrayPriorityQueue()
hospital.insert('Bob', 1)
hospital.insert('Alice', 3)
hospital.insert(None, 1)
for patient in ('Alice', 'Bob', None):  # this is the expected order
    check('find_max', hospital.find_max(), patient, hospital.length())
    hospital.remove_max()

#### Exercise 7.4.4

#### Exercise 7.4.5

#### Exercise 7.4.6

### 7.4.3 With a linked list

### 7.4.4 Min-priority queues

# CELL 5

# %run -i ../m269_priority

reminders = ArrayPriorityQueue()
# meeting with 30 minute advance reminder
reminders.insert('research group meeting @ 3pm', -(14 * 60 + 30))
# meetings with same reminder time
reminders.insert('M269 team meeting @ 11am', -(9 * 60))
reminders.insert('student supervision @ 10am', -(9 * 60))
while reminders.length() > 0:
    print(reminders.find_max())
    reminders.remove_max()

#### Exercise 7.4.7

#### Exercise 7.4.8