# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 16.3 Traversals

# CELL 1

# %run -i ../m269_tree

# MTP is short for minus, times, plus
MTP = join('-', join('*', join('+', THREE, FOUR), FIVE), SIX)

### 16.3.1 Depth-first search

### 16.3.2 Pre-order traversal

# CELL 2

def has(tree: Tree, item: object) -> bool:
    """Return True if and only if the item occurs in the tree."""
    if is_empty(tree):
        return False
    if tree.root == item:   # visit a node
        return True
    return has(tree.left, item) or has(tree.right, item)

has(MTP, 9)

### 16.3.3 In-order traversal

# CELL 3

def infix(expression: Tree) -> None:
    """Print infix form of expression, with full brackets."""
    if is_empty(expression):
        return
    print('(', end='')                  # print nothing after (
    infix(expression.left)
    print(' ', expression.root, ' ', end='')
    infix(expression.right)
    print(')', end='')

infix(MTP)

#### Exercise 16.3.1

# CELL 4

def infix(expression: Tree) -> None:
    """Print infix form of expression, with full brackets."""
    if is_empty(expression):
        return
    print('(', end='')
    infix(expression.left)
    print(' ', expression.root, ' ', end='')
    infix(expression.right)
    print(')', end='')

infix(MTP)  # ((3+4)*5)–6
print()
infix(TPM)  # (3+4)*(5-6)
print()
infix(PMT)  # 3+((4*5)-6)
print()
infix(MPT)  # (3+(4*5))-6

### 16.3.4 Post-order traversal

# CELL 5

def evaluate(expression: Tree) -> int:
    """Return the value of the expression tree.

    Preconditions:
    - expression isn't empty
    - expression only has operators +, -, * and numeric operands
    """
    if is_leaf(expression):
        return expression.root
    left_value = evaluate(expression.left)
    right_value = evaluate(expression.right)
    operator = expression.root
    if operator == '+':
        return left_value + right_value
    if operator == '-':
        return left_value - right_value
    if operator == '*':
        return left_value * right_value

infix(MTP)                  # ((3+4)*5)–6
print(' =', evaluate(MTP))
infix(TPM)                  # (3+4)*(5-6)
print(' =', evaluate(TPM))
infix(PMT)                  # 3+((4*5)-6)
print(' =', evaluate(PMT))
infix(MPT)                  # (3+(4*5))-6
print(' =', evaluate(MPT))

### 16.3.5 Breadth-first search

# CELL 6

# %run -i ../m269_queue

def levels(tree: Tree) -> None:
    """Print the tree from the root down, one level per line."""
    this_level = Queue()
    next_level = Queue()
    this_level.enqueue(tree)
    while this_level.size() > 0:
        tree = this_level.dequeue()
        print(tree.root, ' ', end='')
        if not is_empty(tree.left):
            next_level.enqueue(tree.left)
        if not is_empty(tree.right):
            next_level.enqueue(tree.right)
        # if it was last tree of this level, start new line and level
        if this_level.size() == 0:
            print()
            this_level = next_level
            next_level = Queue()

levels(MTP)    # (3+4) * 5 - 6

# CELL 7

levels(TPM)    # (3+4) * (5-6)