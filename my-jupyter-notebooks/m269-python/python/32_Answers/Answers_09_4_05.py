# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 9.4.5 answer

# CELL 1

# %run -i ../m269_queue
# %run -i ../m269_stack
from algoesup import test

def rearrange(wagons: int, outgoing: list) -> bool:
    """Can the incoming train be rearranged into outgoing?

    Preconditions:
    - wagons > 0
    - outgoing is a permutation of the numbers from 1 to wagons
    """
    east = Queue()
    for wagon in range(1, wagons + 1):
        east.enqueue(wagon)

    west = Queue()
    for wagon in outgoing:
        west.enqueue(wagon)

    station = Stack()
    while west.size() > 0:
        if station.size() > 0 and west.front() == station.peek():
            # move wagon out of station, tick it off the outgoing
            west.dequeue()
            station.pop()
        elif east.size() == 0:
            # no more incoming wagons available
            return False
        else:
            # move incoming wagon to station
            station.push(east.dequeue())
    return True

rearrange_tests = [
    # case,             wagons, outgoing,       rearrange?
    ['keep order',      3,      [1, 2, 3],          True],
    ['invert',          3,      [3, 2, 1],          True],
    ['swap',            3,      [1, 3, 2],          True],
    ['move to front',   5,      [5, 1, 2, 3, 4],    False],
    # new tests:
    ['1 wagon',         1,      [1],                True],
    ['move to back',    4,      [2, 3, 4, 1],       True]
]

test(rearrange, rearrange_tests)