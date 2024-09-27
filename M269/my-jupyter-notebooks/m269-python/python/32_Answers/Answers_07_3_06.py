# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 7.3.6 answer

# CELL 1

# %run -i ../m269_queue

from algoesup import test

def counting_rhyme(n: int) -> int:
    """Return which child from 1 to n remains last in the circle.

    Preconditions: n > 0
    """
    circle = Queue()
    for child in range(1, n+1):
        circle.enqueue(child)
    for round in range(n - 1):
        # in each round, the child on syllable 28 leaves the circle
        for syllable in range(27):
            circle.enqueue(circle.dequeue())
        circle.dequeue()
    return circle.front()

counting_rhyme_tests = [
    # case,         n,  last child
    ['1 child',     1,          1],
    ['2 children',  2,          1],
    ['3 children',  3,          2]
]

test(counting_rhyme, counting_rhyme_tests)