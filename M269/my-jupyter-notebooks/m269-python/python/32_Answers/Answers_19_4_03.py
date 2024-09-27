# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 19.4.3 answer

# CELL 1

from algoesup import test

def max_up_down(numbers: list) -> int:
    """Return the largest of numbers.

    Preconditions:
    - numbers is a non-empty list of non-duplicated integers
    - numbers first ascend and then descend
    - the ascending or the descending part may be empty
    """
    start = 0
    end = len(numbers)      # search in the slice [start:end]
    while end - start > 2:
        middle = start + (end - start) // 2
        # at least 3 numbers, so there's one after the middle one
        if numbers[middle] < numbers[middle+1]:
            # ascending part: maximum comes after the middle
            start = middle + 1
        else:
            # descending part: maximum is middle or to its left
            end = middle + 1
    if end - start == 2:
        return max(numbers[start], numbers[start + 1])
    else:
        return numbers[start]

max_up_down_tests = [
    # case,             numbers,           largest
    ('1 number',        [-1],                  -1),
    ('only descending', [3, 2],                 3),
    ('only ascending',  [-3, -1, 0],            0),
    ('up and down',     [-3, -1, 0, 3, 2, -1],  3),
]

test(max_up_down, max_up_down_tests)