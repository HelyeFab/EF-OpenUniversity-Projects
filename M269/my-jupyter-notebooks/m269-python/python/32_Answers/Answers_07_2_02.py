# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 7.2.2 answer

# CELL 1

# %run -i ../m269_stack

from algoesup import test

def is_balanced(text: str) -> bool:
    """Check if all brackets in text are balanced.

    Preconditions: each bracket in 'text' is one of (, ), [, ]
    """
    opened = Stack()    # opened but not closed brackets
    for character in text:
        if character in '([':
            opened.push(character)
        elif character == ')':
            if opened.size() > 0 and opened.peek() == '(':
                opened.pop()
            else:
                return False
        elif character == ']':
            if opened.size() > 0 and opened.peek() == '[':
                opened.pop()
            else:
                return False
    return opened.size() == 0

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

test(is_balanced, is_balanced_tests)