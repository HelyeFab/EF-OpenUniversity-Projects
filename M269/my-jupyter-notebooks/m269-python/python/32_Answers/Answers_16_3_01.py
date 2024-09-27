# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 16.3.1 answer

# CELL 1

# %run -i ../m269_tree

def infix(expression: Tree) -> None:
    """Print infix form of expression, with full brackets."""
    if is_empty(expression):
        return
    if is_leaf(expression):
        print(expression.root, end='')
        return
    print('(', end='')
    infix(expression.left)
    print(' ', expression.root, ' ', end='')
    infix(expression.right)
    print(')', end='')