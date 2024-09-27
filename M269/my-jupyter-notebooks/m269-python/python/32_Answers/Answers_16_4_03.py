# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 16.4.3 answer

# CELL 1

# %run -i ../m269_tree

def smallest(tree: Tree) -> object:
    """Return the item in the tree with the smallest key.
    """
    while not is_empty(tree.left):
        tree = tree.left
    return tree.root