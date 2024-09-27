# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 13.5.1 answer

# CELL 1

def first_positive(numbers: list) -> int:
    def in_slice(start: int, end: int) -> int:
        """Return the first positive number within numbers[start:end].

        Preconditions: 0 <= start < end <= len(items)
        """
        if end - start == 1:
            return numbers[start]
        elif end - start == 2:
            if numbers[start] > 0:
                return numbers[start]
            else:
                return numbers[start + 1]
        else:
            middle = start + (end - start) // 2
            if numbers[middle] > 0:
                return in_slice(start, middle + 1)  # include middle
            else:
                return in_slice(middle + 1, end)

    return in_slice(0, len(numbers))