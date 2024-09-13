# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 2.8.2 answer

# CELL 1

left =  2222
right = 7777
# %timeit -r 6 -n 2000000 left % right   # 4 digits
left =  22222222
right = 77777777
# %timeit -r 6 -n 2000000 left % right   # 8 digits
left =  2222222222222222
right = 7777777777777777
# %timeit -r 6 -n 2000000 left % right   # 16 digits
left =  22222222222222222222222222222222
right = 77777777777777777777777777777777
# %timeit -r 6 -n 2000000 left % right   # 32 digits
left =  2222222222222222222222222222222222222222222222222222222222222222
right = 7777777777777777777777777777777777777777777777777777777777777777
# %timeit -r 6 -n 2000000 left % right   # 64 digits

# CELL 2

left =  7777
right = 2222
# %timeit -r 6 -n 2000000 left % right   # 4 digits
left =  77777777
right = 22222222
# %timeit -r 6 -n 2000000 left % right   # 8 digits
left =  7777777777777777
right = 2222222222222222
# %timeit -r 6 -n 2000000 left % right   # 16 digits
left =  77777777777777777777777777777777
right = 22222222222222222222222222222222
# %timeit -r 6 -n 2000000 left % right   # 32 digits
left =  7777777777777777777777777777777777777777777777777777777777777777
right = 2222222222222222222222222222222222222222222222222222222222222222
# %timeit -r 6 -n 2000000 left % right   # 64 digits