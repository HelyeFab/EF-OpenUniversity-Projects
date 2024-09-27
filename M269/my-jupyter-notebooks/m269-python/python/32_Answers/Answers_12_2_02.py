# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 12.2.2 answer

# CELL 1

from algoesup import test

def even(n: int) -> bool:
    """Return True if and only if n is divisible by 2.

    Preconditions: n > 0
    """
    if n == 1:
        return False
    else:
        return not even(n-1)

even_tests = [
    # case,             n,      even?
    ('smallest even',   2,      True),
    ('larger even',     100,    True),
    # your tests here
    ('smallest input',  1,      False),
    ('larger odd',      45,     False)
]

test(even, even_tests)