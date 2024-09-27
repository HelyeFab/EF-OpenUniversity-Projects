# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 2.3 Expressions

# CELL 1

(-2) ** 0

### 2.3.1 Mistakes

# CELL 2

2 ** 3 ** 2     # this is evaluated right to left

# CELL 3

(2 ** 3) ** 2   # use parentheses to force left-to-right evaluation

#### Exercise 2.3.1