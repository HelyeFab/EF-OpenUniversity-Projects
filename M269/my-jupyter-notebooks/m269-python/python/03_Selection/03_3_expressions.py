# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 3.3 Boolean expressions

### 3.3.1 Comparisons

# CELL 1

3 == 5

# CELL 2

True == 42  # any values can be compared

# CELL 3

False == False

# CELL 4

3 != 5

# CELL 5

True != 42  # any values can be compared

# CELL 6

False != False

# CELL 7

4 >= 3.5

# CELL 8

51 - 20 == 29 + 2 and not False

# CELL 9

numerator = 5
denominator = 0
is_probability = denominator != 0 and 0 <= numerator / denominator <= 1
is_probability

# CELL 10

# %timeit -r 3 -n 1000 9 > 8
# %timeit -r 3 -n 1000 9_999_999 > 9_999_998
# %timeit -r 3 -n 1000 9 != False
# %timeit -r 3 -n 1000 9_999_999 != False

### 3.3.2 Mistakes

# CELL 11

True = 42

# CELL 12

4 > = 3

# CELL 13

0.1 + 0.2 == 0.3

# CELL 14

margin = 0.001
0.3 - margin <= 0.1 + 0.2 <= 0.3 + margin

# CELL 15

False == not True

#### Exercise 3.3.1

#### Exercise 3.3.2