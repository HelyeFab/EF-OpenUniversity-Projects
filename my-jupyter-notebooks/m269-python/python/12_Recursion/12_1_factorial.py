# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 12.1 The factorial function

### 12.1.1 Definition and algorithm

### 12.1.2 Code

# CELL 1

def factorial(n: int) -> int:
    """Return the factorial of n.

    Preconditions: n >= 0
    Postconditions:
    - if n = 0, then the output is 1
    - otherwise the output is 1*2*...*(n-1)*n.
    """
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

factorial(5)

# CELL 2

def factorial_printed(n: int, level: int) -> int:
    """Return the factorial of n.

    Preconditions: n >= 0, level >= 0
    Postconditions: the output is 1 for n=0, otherwise 1*...*(n-1)*n
    """
    print('    ' * level, 'factorial of', n, '=')
    if n == 0:
        print('    ' * level, 1)
        return 1
    else:
        product = factorial_printed(n-1, level+1) * n
        print('    ' * level, '*', n, '=', product)
        return product

factorial_printed(3, 0)

### 12.1.3 The call stack

# CELL 3

factorial(3000)