# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 3.2.3 answer

# CELL 1

def internet_connection(in_flight_mode: bool,
                        wifi_on: bool,
                        data_on: bool) -> bool:
    internet_on = (not in_flight_mode) and (wifi_on or data_on)
    return internet_on

# %timeit -r 3 -n 1000 internet_connection(False, True, False)
# %timeit -r 3 -n 1000 internet_connection(False, True, True)