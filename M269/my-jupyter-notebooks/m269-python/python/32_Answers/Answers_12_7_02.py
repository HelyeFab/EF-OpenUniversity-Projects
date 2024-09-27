# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 12.7.2 answer

# CELL 1

def has(items: list, item: object) -> bool:
    """Return True if and only if item is a member of items."""

    def in_slice(start: int, end: int) -> bool:
        """Return True if and only if item is in slice items[start:end].

        Preconditions: 0 <= start <= end <= len(items)
        """
        if start == end:
            return False
        elif start + 1 == end:
            return items[start] == item
        else:
            middle = start + (end - start) // 2
            exists_left = in_slice(start, middle)
            exists_right = in_slice(middle, end)
            return exists_left or exists_right

    return in_slice(0, len(items))