# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 4.4.5 answer

# CELL 1

def valid_password(password: str) -> bool:
    """Return whether password has a digit and a lowercase letter."""
    has_letter = False
    has_digit = False
    for character in password:
        if '0' <= character <= '9':
            has_digit = True
        if 'a' <= character <= 'z':
            has_letter = True
        if has_letter and has_digit:
            return True
    return False

# CELL 2

not valid_password('')

# CELL 3

valid_password('a5')

# CELL 4

not valid_password('MK 01908')

# CELL 5

not valid_password('päßword')

# CELL 6

not valid_password('^+-/&?')

# CELL 7

valid_password('my_P455W0RD')