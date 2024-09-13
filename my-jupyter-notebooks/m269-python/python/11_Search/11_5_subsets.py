# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 11.5 Searching subsets

### 11.5.1 Problem

# CELL 1

feasible_products_tests = [
    # case,             features,     incompatible, products
    ('smallest input',  {1},          {},                 1),
    ('all compatible',  {1, 2},       {},                 3),
    ('no compatible',   {1, 2},       {(1, 2)},           2),
    ('some compatible', {1, 2, 3, 4}, {(1, 2), (3, 4)},   8)
]

### 11.5.2 Algorithm

#### Exercise 11.5.1

### 11.5.3 Complexity

# CELL 2

from math import factorial

MS_PER_YEAR = 365 * 24 * 60 * 60 * 1000     # milliseconds in a year
print(factorial(25) // MS_PER_YEAR // 1000**3, 'billion years')

### 11.5.4 Code

# CELL 3

from itertools import combinations

items = {'some', 'words'}
for size in range(len(items) + 1):
    for subset in combinations(items, size):
        print(subset)

# CELL 4

from itertools import combinations
from algoesup import test

def feasible_products(features: set, incompatible: set) -> int:
    """Return the number of subsets of features without incompatibilities.

    Preconditions:
    - len(features) > 0
    - incompatible is a set of pairs of distinct elements of features
    - if pair (a, b) is in incompatible, pair (b, a) isn't
    """

    def feasible(product: tuple) -> bool:
        """Check if product hasn't two incompatible features."""
        for pair in incompatible:
            if pair[0] in product and pair[1] in product:
                return False
        return True

    products = 0
    for size in range(1, len(features) + 1):
        for product in combinations(features, size):
            if feasible(product):
                products = products + 1
    return products

test(feasible_products, feasible_products_tests)

#### Exercise 11.5.2