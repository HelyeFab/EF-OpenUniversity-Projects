# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 3.5.10 answer

# CELL 1

def is_leap_year(year: int) -> bool:
    """Return whether the given year is a leap year.

    Preconditions: year > 1582
    Postconditions: return true if and only if
    year is divisible by 4 but not by 100, or is divisible by 400
    """
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# CELL 2

is_leap_year(1600) == True

# CELL 3

is_leap_year(1700) == False

# CELL 4

is_leap_year(2020) == True

# CELL 5

is_leap_year(1583) == False