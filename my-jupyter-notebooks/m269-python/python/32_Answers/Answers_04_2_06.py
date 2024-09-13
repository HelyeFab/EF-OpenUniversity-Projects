# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 4.2.6 answer

# CELL 1

text = 'hello'
times = 3
(text + '...') * (times - 1) + text

# CELL 2

text = 'hello'
times = 3
((text + '...') * times)[:-3]   # whole string without last 3 dots