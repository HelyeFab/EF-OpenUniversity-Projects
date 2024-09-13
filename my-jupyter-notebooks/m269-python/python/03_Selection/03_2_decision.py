# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 3.2 Decision problems

### 3.2.1 Problem definition

### 3.2.2 Problem instances

#### Exercise 3.2.1

### 3.2.3 Algorithm

### 3.2.4 Complexity

### 3.2.5 Code and tests

# CELL 1

def internet_connection(in_flight_mode: bool,
                        wifi_on: bool,
                        data_on: bool) -> bool:
    """Return whether there's a connection to the internet.

    Postconditions: the output is true if and only if
    (not in_flight_mode) and (wifi_on or data_on)
    """
    internet_on = (not in_flight_mode) and (wifi_on or data_on)
    return internet_on

# CELL 2

internet_connection(True, True, True)

# CELL 3

internet_connection(False, False, False)

# CELL 4

internet_connection(False, True, False)

# CELL 5

internet_connection(False, False, True)

# CELL 6

internet_connection(False, True, True)

#### Exercise 3.2.2

### 3.2.6 Performance

# CELL 7

# %timeit -r 3 -n 1000 internet_connection(True, True, True)
# %timeit -r 3 -n 1000 internet_connection(False, False, False)

# CELL 8

# %timeit -r 3 -n 1000 internet_connection(False, False, False)
# %timeit -r 3 -n 1000 internet_connection(False, False, True)

#### Exercise 3.2.3

# CELL 9

# replace with your code