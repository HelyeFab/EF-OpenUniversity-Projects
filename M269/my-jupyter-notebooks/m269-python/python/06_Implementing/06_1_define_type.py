# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 6.1 Defining data types

### 6.1.1 Data structure

### 6.1.2 Functions

# CELL 1

def fraction(numerator: int, denominator: int) -> tuple:
    return (numerator, denominator)

def multiplication(left: tuple, right: tuple) -> tuple:
    return (left[0] * right[0], left[1] * right[1])

# CELL 2

half = fraction(1, 2)
multiplication(half, half)  # one half times one half is a quarter

# CELL 3

multiplication((1, 2), (1, 3, 5))

### 6.1.3 Classes

# CELL 4

class Fraction:
    """A ratio represented as a pair of integers:
    a numerator and a non-zero denominator.
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialise the fraction.

        Preconditions: denominator != 0
        """
        self.value = (numerator, denominator)

    def multiplication(self, right: 'Fraction') -> 'Fraction':
        """Return the product of self and right.

        Postconditions: if self is the fraction sn/sd and
        right is the fraction rn/rd, then the output is fraction
        (sn*rn) / (sd*rd)
        """
        numerator = self.value[0] * right.value[0]
        denominator = self.value[1] * right.value[1]
        return Fraction(numerator, denominator)

# CELL 5

one_half = Fraction(1, 2)

# CELL 6

help(Fraction)

# CELL 7

one_half.multiplication(one_half)

# CELL 8

print(one_half.multiplication(one_half))

# CELL 9

class Fraction:
    """A number represented as a pair of integers:
    a numerator and a non-zero denominator.
    """

    def __init__(self, numerator: int, denominator: int):
        """Initialise the fraction.

        Preconditions: denominator != 0
        """
        self.value = (numerator, denominator)

    def multiplication(self, right: 'Fraction') -> 'Fraction':
        """Return the product of self and right.

        Postconditions: if self is the fraction sn/sd and
        right is the fraction rn/rd, then the output is fraction
        (sn*rn) / (sd * rd)
        """
        numerator = self.value[0] * right.value[0]
        denominator = self.value[1] * right.value[1]
        return Fraction(numerator, denominator)

    def __str__(self) -> str:
        """Return a string representation of the fraction."""
        return str(self.value[0]) + ' / ' + str(self.value[1])

# CELL 10

ONE_HALF = Fraction(1, 2)
ONE_QUARTER = ONE_HALF.multiplication(ONE_HALF)
ONE_QUARTER         # display class and unique id

# CELL 11

print(ONE_QUARTER)
str(ONE_QUARTER)

### 6.1.4 Mistakes

# CELL 12

print(half)         # created with fraction(1, 2); instance of tuple
print(one_half)     # created with first version of Fraction class
print(ONE_HALF)     # created with second version of Fraction class

# CELL 13

class Date:
    # docstrings and __init__ omitted to focus on the issue at hand

    def difference(self, other: Date) -> int:
        """Return number of days between two dates."""
        return 0    # dummy code

# CELL 14

__str__(ONE_QUARTER)

# CELL 15

ONE_QUARTER.__str__()

# CELL 16

multiplication(ONE_HALF, ONE_HALF)

# CELL 17

one_half.multiplication( (1, 2) )

# CELL 18

class Date:

    def __init__(self):
        self.day = 1

    def day(self) -> int:
        return self.day

# CELL 19

Date().day

# CELL 20

Date().day()

# CELL 21

if 0 < ONE_HALF.value[0] < ONE_HALF.value[1]:
    print(ONE_HALF, 'is positive and smaller than 1')

# CELL 22

class Fraction:
    # docstrings omitted to focus on data structure changes

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def multiplication(self, right: 'Fraction') -> 'Fraction':
        numerator = self.numerator * right.numerator
        denominator = self.denominator * right.denominator
        return Fraction(numerator, denominator)

    def __str__(self) -> str:
        return str(self.numerator) + ' / ' + str(self.denominator)

print(Fraction(1, 2).multiplication(Fraction(1, 3)))

# CELL 23

class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.top = numerator
        self.denominator = denominator

    def numerator(self) -> int:
        return self.top

    def multiplication(self, right: 'Fraction') -> 'Fraction':
        numerator = self.numerator() * right.numerator()
        denominator = self.denominator * right.denominator
        return Fraction(numerator, denominator)

    def __str__(self) -> str:
        return str(self.numerator()) + ' / ' + str(self.denominator)

print(Fraction(1, 2).multiplication(Fraction(1, 3)))