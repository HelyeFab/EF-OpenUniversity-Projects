# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 7.4.3 answer

# CELL 1

# this code is also in m269_priority.py

class ArrayPriorityQueue:

    def insert(self, item: object, priority: object) -> None:
        index = 0
        while index < len(self.priorities) and self.priorities[index] < priority:
            index = index + 1
        self.items.insert(index, item)
        self.priorities.insert(index, priority)