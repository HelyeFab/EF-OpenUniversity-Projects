# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 16.4 Binary search trees

# CELL 1

# %run -i ../m269_tree

KEY = 0
VALUE = 1

# CELL 2

I = (1, 'I')
IV = (4, 'IV')
V = (5, 'V')
VI = (6, 'VI')
VIII = (8, 'VIII')

one = join(I, Tree(), Tree())
six = join(VI, Tree(), Tree())
bst = join(IV, one, join(VIII, join(V, Tree(), six), Tree()))

### 16.4.1 Search

# CELL 3

def has(tree: Tree, key: object) -> bool:
    """Return True if and only if a node of tree has the key.

    Preconditions: tree is a BST
    """
    if is_empty(tree):
        return False
    elif tree.root[KEY] == key:
        return True
    elif tree.root[KEY] < key:
        return has(tree.right, key)
    else:
        return has(tree.left, key)

has(bst, 2)

# CELL 4

has(bst, 6)

#### Exercise 16.4.1

# CELL 5

from algoesup import test

def lookup(tree: Tree, key: object) -> object:
    """Return the value associated to the key.

    Preconditions: tree is a BST and has the key"""
    pass

lookup_tests = [
    ('key in leaf',   bst, 1, 'I'),
    ('key in root',   bst, 4, 'IV'),
    ('key in other',  bst, 5, 'V')
]

test(lookup, lookup_tests)

#### Exercise 16.4.2

#### Exercise 16.4.3

# CELL 6

def smallest(tree: Tree) -> object:
    """Return the item in the tree with the smallest key.

    Preconditions: tree is a non-empty BST
    """
    pass

# CELL 7

smallest(bst) == I

# CELL 8

smallest(six) == VI    # this tree has a single node

### 16.4.2 Add node

# CELL 9

def associate(tree: Tree, key: object, value: object) -> None:
    """Associate the value to the key in the tree.

    Preconditions: tree is a BST
    Postconditions:
    - if there's a node with the key, replace its value with the given one
    - otherwise, add the key-value pair to the tree
    """
    # Base case: if tree is empty, create a leaf
    if is_empty(tree):
        tree.root = (key, value)
        tree.left = Tree()
        tree.right = Tree()
    # Base case: if the key is in the root, replace the value
    elif tree.root[KEY] == key:
        tree.root = (key, value)
    # Recurrence relation: add/replace in the appropriate subtree
    elif tree.root[KEY] < key:
        associate(tree.right, key, value)
    else:
        associate(tree.left, key, value)

# CELL 10

def write(tree: Tree, level: int) -> None:
    """Print the tree as in file browsers, with subtrees indented.

    Preconditions: level >= 0 is the initial indentation level
    """
    if is_empty(tree):
        print(' ' * 4 * level, 'EMPTY')
    else:
        print(' ' * 4 * level, tree.root)
        write(tree.left, level + 1)
        write(tree.right, level + 1)

write(bst, 0)   # compare the output to the left tree in Figure 16.4.1

# CELL 11

associate(bst, 2, 'II')
write(bst, 0)

### 16.4.3 Remove node

# CELL 12

def smallest(tree: Tree) -> object:
    """Return the item in the tree with the smallest key.

    Preconditions: tree is a non-empty BST
    """
    while not is_empty(tree.left):
        tree = tree.left
    return tree.root

def remove(tree: Tree, key: object):
    """Remove the tree's node with the key.

    Do nothing if there's no such node.
    """
    if is_empty(tree):
        pass                        # key not found
    elif tree.root[KEY] < key:
        remove(tree.right, key)
    elif key < tree.root[KEY]:
        remove(tree.left, key)
    else:                           # key found: it's in the root
        if is_empty(tree.left):     # replace tree with right subtree
            tree.root = tree.right.root
            tree.left = tree.right.left
            tree.right = tree.right.right
        elif is_empty(tree.right):    # replace tree with left subtree
            tree.root = tree.left.root
            tree.right = tree.left.right    # note different order
            tree.left = tree.left.left      # of assignments
        else:                       # replace root with successor
            tree.root = smallest(tree.right)
            remove(tree.right, tree.root[KEY])

# CELL 13

remove(bst, 2)
write(bst, 0)

# CELL 14

remove(bst, 4)
write(bst, 0)