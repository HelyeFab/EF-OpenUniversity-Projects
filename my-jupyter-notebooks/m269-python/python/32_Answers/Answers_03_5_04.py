# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 3.5.4 answer

# CELL 1

def calls_possible(flight_mode: bool, signal_strength: int) -> bool:
    """Return whether the phone can make and receive calls.

    Preconditions: 0 <= signal_strength <= 4
    Postconditions: the output is true if and only if
    flight_mode is false and signal_strength >= 2
    """
    return (not flight_mode) and (signal_strength >= 2)

# CELL 2

calls_possible(False, 1) == False

# CELL 3

calls_possible(False, 2) == True

# CELL 4

calls_possible(True, 4) == False