# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 3.4 Classification problems

### 3.4.1 Problem definition and instances

### 3.4.2 Algorithm

#### Exercise 3.4.1

#### Exercise 3.4.2

#### Exercise 3.4.3

### 3.4.3 Complexity

### 3.4.4 Code

# CELL 1

def grading(mark: int) -> int:
    """Return the pass grade, from 1 to 5, for the given mark.

    Preconditions: 0 <= mark <= 100
    Postconditions:
    - if mark < 40, return 5
    - if 40 <= mark < 50, return 4
    - if 50 <= mark < 60, return 3
    - if 60 <= mark < 80, return 2
    - if mark >= 80, return 1
    """
    if mark < 40:
        grade = 5
    elif mark < 50:
        grade = 4
    elif mark < 60:
        grade = 3
    elif mark < 80:
        grade = 2
    else:
        grade = 1
    return grade

### 3.4.5 Tests

# CELL 2

grading(0) == 5

# CELL 3

grading(39) == 5

# CELL 4

grading(40) == 4

# CELL 5

grading(49) == 4

# CELL 6

grading(50) == 3

# CELL 7

grading(59) == 3

# CELL 8

grading(60) == 2

# CELL 9

grading(79) == 2

# CELL 10

grading(80) == 1

# CELL 11

grading(100) == 1

### 3.4.6 Performance

# CELL 12

# %timeit -r 3 -n 1000 grading(0)
# %timeit -r 3 -n 1000 grading(100)

### 3.4.7 Mistakes