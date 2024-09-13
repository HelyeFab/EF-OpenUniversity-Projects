# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 12.6.3 answer

# CELL 1

def maximum(numbers: list) -> int:
    """Return the largest number in numbers.

    Preconditions: numbers is a non-empty list of integers
    """
    def in_slice(start: int, end: int) -> int:
        """Return the largest integer in slice numbers[start:end].

        Preconditions: 0 <= start < end <= len(items)
        """
        if start + 1 == end:
            return numbers[start]
        else:
            return max(numbers[start], in_slice(start+1, end))

    return in_slice(0, len(numbers))