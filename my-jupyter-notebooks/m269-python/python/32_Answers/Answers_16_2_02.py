# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 16.2.2 answer

# CELL 1

# %run -i ../m269_tree
from algoesup import test

def height(tree: Tree) -> int:
    """Return the height of the tree."""
    if is_empty(tree):
        return 0
    else:
        return max(height(tree.left), height(tree.right)) + 1

height_tests = [
    # case,         tree,   height
    ('empty',       EMPTY,  0),
    ('(3+4)*(5-6)',   TPM,  3),
    ('3+((4*5)-6)',   PMT,  4),
    ('(3+(4*5))-6',   MPT,  4),
]

test(height, height_tests)