# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 6.3.1 answer

# CELL 1

class Sequence:
    """The sequence ADT."""

    def has(self, item: object) -> bool:
        """Return True if and only if item is a member of self."""
        for index in range(self.length()):
            if self.get_item(index) == item:
                return True
        return False