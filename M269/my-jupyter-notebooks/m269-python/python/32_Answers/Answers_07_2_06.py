# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 7.2.6 answer

# CELL 1

# %run -i ../m269_stack

from algoesup import test

def evaluate(expression: list) -> int:
    """Return the value of the given postfix expression.

    Preconditions:
    - each item in the input list is a natural number, '-' or '*'
    - the input represents a valid non-empty postfix expression
    """
    values = Stack()
    for item in expression:
        if item == '-':
            right = values.pop()
            left = values.pop()
            values.push(left - right)
        elif item == '*':
            right = values.pop()
            left = values.pop()
            values.push(left * right)
        else:       # it's an operand
            values.push(item)
    return values.peek()

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