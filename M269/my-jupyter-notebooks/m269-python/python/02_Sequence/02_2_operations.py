# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 2.2 Arithmetic operations

### 2.2.1 On real numbers

### 2.2.2 On integers

#### Exercise 2.2.1

### 2.2.3 On `int` and `float`

# CELL 1

6 / 3

# CELL 2

2 + 3

# CELL 3

2.0 + 3

# CELL 4

2 * -3

# CELL 5

import math
max(3, math.pi, -0.5)

# CELL 6

min(3, math.pi, -0.5)

### 2.2.4 On `float`

# CELL 7

math.floor(1.5)

# CELL 8

math.floor(-1.5)

### 2.2.5 On `int`

# CELL 9

2 / -3      # one slash: float division

# CELL 10

2 // -3     # two slashes: floor division

# CELL 11

2 // 3

# CELL 12

5 % 2

# CELL 13

-5 % 2

# CELL 14

5 % -2

# CELL 15

-2 ** 3

### 2.2.6 Mistakes

# CELL 16

2 % 0

# CELL 17

2 / / 3

# CELL 18

-2 ** 0     # expecting x⁰ = 1 for all x