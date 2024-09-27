# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 3.1 Booleans

### 3.1.1 The Boolean ADT

#### Exercise 3.1.1

#### Exercise 3.1.2

### 3.1.2 Using Booleans

#### Exercise 3.1.3

#### Exercise 3.1.4

### 3.1.3 The `bool` type

# CELL 1

True and not True or True

# CELL 2

phone_on = False
phone_on = not phone_on
phone_on

#### Exercise 3.1.5

# CELL 3

True and not True or True

#### Exercise 3.1.6

### 3.1.4 Mistakes

# CELL 4

is_tall = False
blue_eyes = False
brown_eyes = True
is_tall and blue_eyes or brown_eyes

# CELL 5

is_tall and (blue_eyes or brown_eyes)

# CELL 6

is_tall and blue_eys or brown_eyes

#### Exercise 3.1.7