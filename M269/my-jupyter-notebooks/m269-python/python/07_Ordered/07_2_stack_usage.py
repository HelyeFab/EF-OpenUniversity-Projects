# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 7.2 Using stacks

### 7.2.1 Balanced brackets

# CELL 1

('hello'[1:3 + 'h')] * 3    # brackets within () aren't balanced

# CELL 2

is_balanced_tests = [
    # case,         text,                               balanced
    ['no text',     '',                                 True],
    ['no brackets', 'brackets are like Russian dolls',  True],
    ['matched',     '(3 + 4)',                          True],
    ['mismatched',  '(3 + 4]',                          False],
    ['not opened',  '3 + 4]',                           False],
    ['not closed',  '(3 + 4',                           False],
    ['wrong order', 'close ) before open (',            False],
    ['nested',      '([([])])',                         True],
    ['nested pair', 'items[(i - 1):(i + 1)]',           True]
]

#### Exercise 7.2.1

#### Exercise 7.2.2

# CELL 3

# %run -i ../m269_stack

from algoesup import test

def is_balanced(text: str) -> bool:
    """Check if all brackets in text are balanced.

    Preconditions: each bracket in 'text' is one of (, ), [, ]
    """
    pass

test(is_balanced, is_balanced_tests)

#### Exercise 7.2.3

### 7.2.2 Postfix expressions

#### Exercise 7.2.4

#### Exercise 7.2.5

#### Exercise 7.2.6

# CELL 4

# %run -i ../m269_stack

from algoesup import test

def evaluate(expression: list) -> int:
    """Return the value of the given postfix expression.

    Preconditions:
    - each item in the input list is a natural number, '-' or '*'
    - the input represents a valid non-empty postfix expression
    """
    pass

evaluate_tests = [
    # case,             expression,                     value
    ['3 * 4',           [3, 4, '*'],                    12],
    ['3 - 4',           [3, 4, '-'],                    -1],
    ['3 - 4 * 5',       [3, 4, 5, '*', '-'],            -17],
    ['(3 - 4) * 5',     [3, 4, '-', 5, '*'],            -5],
    ['(3 - 4) * (5 - 6)', [3, 4, '-', 5, 6, '-', '*'],  1],
    ['no operation',    [4],                            4]
]

test(evaluate, evaluate_tests)