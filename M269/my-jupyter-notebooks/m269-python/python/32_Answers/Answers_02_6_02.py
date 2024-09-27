# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 2.6.2 answer

# CELL 1

def total_price(price: float, vat_rate: float) -> float:
    """Return the total price, including VAT at the given rate.

    Preconditions:
    - price > 0 and price is in euros
    - 0 <= vat_rate < 1
    Postconditions:
    - the output is price * (1 + vat_rate)
    - the output is in euros
    """
    return price * (1 + vat_rate)

total_price(100, 0.2)