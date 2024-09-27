# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 8.4 Sets

### 8.4.1 The set ADT

### 8.4.2 Sets in Python

# CELL 1

odd = {1, 3, 5}
even = {2, 4, 6}
prime = {2, 3, 5}
print('all:', odd | even)
print('even primes:', even & prime)
print("odd primes (primes that aren't even):", prime - even)
print("even numbers that aren't prime:", even - prime)

#### Exercise 8.4.1

# CELL 2

print('all:', odd | even | prime)
print("odd numbers that aren't even primes", odd - (prime & even))
print("non-prime odd numbers that are even:", odd - prime & even)
print("prime numbers that are odd or even", (odd | even) & prime)
print("numbers that are even primes or odd", odd | even & prime)

# CELL 3

print('are all primes odd?', prime <= odd)
print('are all odd numbers prime?', odd <= prime)
print('are some numbers not prime?', prime < odd | even)

# CELL 4

set([3, 4, 3, 6, 2, 1, 6])

# CELL 5

unique = set()
for item in [3, 4, 3, 6, 2, 1, 6]:
    unique.add(item)
unique

### 8.4.3 Implementing sets

#### Exercise 8.4.2

#### Exercise 8.4.3

### 8.4.4 Using sets

#### Exercise 8.4.4

# CELL 6

from algoesup import test

def certificates(ranking: list) -> list:
    """Return the best team of each school.

    The input and output are lists of strings (team names).
    Each string is the name of a school and a digit from 1 to 4.

    Preconditions:
    - ranking is a non-empty list ordered from first to last team
    - there are no duplicate teams
    Postconditions:
    - the output has the first team in 'ranking' of each school
    - the output strings are in the same order as in 'ranking'
    """
    best_teams = []
    pass
    return best_teams

certificates_tests = [
    # case,         ranking,                    certificates
    ('3 schools',   ['C1','B2','B1','A1','C2'], ['C1','B2','A1']),
    # new tests:
]

test(certificates, certificates_tests)