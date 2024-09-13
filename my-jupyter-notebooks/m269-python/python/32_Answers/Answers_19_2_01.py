# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 19.2.1 answer

# CELL 1

from math import factorial

NS_PER_YEAR = 365 * 24 * 60 * 60 * 1000 * 1000 * 1000   # nanoseconds in a year
print(factorial(20) * 20 // NS_PER_YEAR, 'years')