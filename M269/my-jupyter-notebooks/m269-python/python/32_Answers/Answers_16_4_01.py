# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 16.4.1 answer

# CELL 1

# %run -i ../m269_tree

def lookup(tree: Tree, key: object) -> object:
    """Return the value associated to the key.

    Preconditions: tree is a BST and has the key"""
    if tree.root[KEY] == key:
        return tree.root[VALUE]
    elif tree.root[KEY] < key:
        return lookup(tree.right, key)
    else:
        return lookup(tree.left, key)