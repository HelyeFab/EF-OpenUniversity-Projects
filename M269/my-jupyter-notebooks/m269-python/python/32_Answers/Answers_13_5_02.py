# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 13.5.2 answer

# CELL 1

def first_positive(numbers: list) -> int:
    start = 0
    end = len(numbers)
    while end - start > 2:
        middle = start + (end - start) // 2
        if numbers[middle] > 0:
            end = middle + 1
        else:
            start = middle + 1
    if numbers[start] > 0:
        return numbers[start]
    else:
        return numbers[start + 1]