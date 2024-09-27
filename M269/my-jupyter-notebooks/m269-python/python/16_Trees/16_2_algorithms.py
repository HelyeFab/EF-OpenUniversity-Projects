# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 16.2 Algorithms on trees

### 16.2.1 Divide and conquer

# CELL 1

# %run -i ../m269_tree

# CELL 2

# this code is also in m269_tree.py

def size(tree: Tree) -> int:
    """Return the number of nodes in tree."""
    if is_empty(tree):
        return 0
    else:
        return size(tree.left) + size(tree.right) + 1

# CELL 3

size(TPM)

#### Exercise 16.2.1

#### Exercise 16.2.2

# CELL 4

# %run -i ../m269_tree
from algoesup import test

def height(tree: Tree) -> int:
    """Return the height of the tree."""
    pass

height_tests = [
    # case,         tree,   height
    ('empty',       EMPTY,  0),
    ('(3+4)*(5-6)',   TPM,  3),
    ('3+((4*5)-6)',   PMT,  4),
    ('(3+(4*5))-6',   MPT,  4),
]

test(height, height_tests)

### 16.2.2 Arm's-length recursion

# CELL 5

def size_arm(tree: Tree) -> int:
    """Return the size of the tree using arm's length recursion."""
    if is_empty(tree):
        return 0
    elif is_leaf(tree):                 # both subtrees empty
        return 1
    elif is_empty(tree.left):           # left subtree empty
        return size_arm(tree.right) + 1
    elif is_empty(tree.right):          # right subtree empty
        return size_arm(tree.left) + 1
    else:
        return size_arm(tree.left) + size_arm(tree.right) + 1

# CELL 6

tree = join('leaf', EMPTY, EMPTY)
for level in range(1000):
    tree = join('a node', tree, EMPTY)

# %timeit -r 5 size(tree)
# %timeit -r 5 size_arm(tree)