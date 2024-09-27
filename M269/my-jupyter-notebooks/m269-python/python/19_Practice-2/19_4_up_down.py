# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 19.4 Up and down

### 19.4.1 Exercises

#### Exercise 19.4.1

#### Exercise 19.4.2

#### Exercise 19.4.3

# CELL 1

from algoesup import test

def max_up_down(numbers):
    pass

max_up_down_tests = [
    # case,             numbers,           largest
    ('1 number',        [-1],                  -1),
    ('only descending', [3, 2],                 3),
    ('only ascending',  [-3, -1, 0],            0),
    ('up and down',     [-3, -1, 0, 3, 2, -1],  3),
]

test(max_up_down, max_up_down_tests)