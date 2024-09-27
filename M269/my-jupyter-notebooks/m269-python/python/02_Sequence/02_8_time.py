# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 2.8 Run-times

# CELL 1

# %timeit 2 + 7

# CELL 2

# %timeit -r 5 -n 1000000 2 + 7

# CELL 3

# %timeit -r 5 -n 1000000 (2 ** 64 + 1) + (2 ** 64 + 2)

# CELL 4

left = 2
right = 7
# %timeit -r 5 -n 1000000 left + right
left = 2 ** 64 + 1
right = 2 ** 64 + 2
# %timeit -r 5 -n 1000000 left + right

# CELL 5

left = 9876543210
right = 123456789
# %timeit -r 5 -n 1000000 left + right
# %timeit -r 5 -n 1000000 left // right

# CELL 6

def brick_volume(length: int, width: int, height: int) -> int:
    return length * width * height

l = 2
w = 3
h = 4
# %timeit -r 5 brick_volume(l, w, h)

### 2.8.1 Checking growth rates

# CELL 7

left =  2
right = 7
# %timeit -r 5 -n 1000000 left + right  # 1 digit
left =  22
right = 77
# %timeit -r 5 -n 1000000 left + right  # 2 digits
left =  2222
right = 7777
# %timeit -r 5 -n 10000 left + right  # 4 digits
left =  22222222
right = 77777777
# %timeit -r 5 -n 10000 left + right  # 8 digits
left =  2222222222222222
right = 7777777777777777
# %timeit -r 5 -n 10000 left + right  # 16 digits
left =  22222222222222222222222222222222
right = 77777777777777777777777777777777
# %timeit -r 5 -n 10000 left + right  # 32 digits
left =  2222222222222222222222222222222222222222222222222222222222222222
right = 7777777777777777777777777777777777777777777777777777777777777777
# %timeit -r 5 -n 10000 left + right  # 64 digits

# CELL 8

base = 5
# %timeit -r 5 -n 10000 base ** 1
# %timeit -r 5 -n 10000 base ** 2
# %timeit -r 5 -n 10000 base ** 4
# %timeit -r 5 -n 10000 base ** 8
# %timeit -r 5 -n 10000 base ** 16
# %timeit -r 5 -n 10000 base ** 32
# %timeit -r 5 -n 10000 base ** 64

#### Exercise 2.8.1

#### Exercise 2.8.2