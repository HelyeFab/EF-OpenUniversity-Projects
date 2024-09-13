# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 9.3 Voucher

# CELL 1

from algoesup import test

def pairs(store: list, voucher: int) -> set:
    """Return all pairs of products that together cost voucher.

    A product is represented by a string–integer tuple:
    the product's name and its positive price.
    Store is a list of products.
    The output is a set of product pairs (tuples).

    Preconditions: voucher > 0

    Postconditions: for each (p1, p2) in the output,
    - p1 and p2 occur in store
    - p1 doesn't occur after p2 in store
    - the price of p1 + the price of p2 == voucher
    """
    results = set()
    pass
    return results

F1 = ('food', 1)
F2 = ('food', 2)
F5 = ('food', 5)
F6 = ('food', 6)
T5 = ('toy', 5)

pairs_tests = [
    # case,         store,          voucher, results
    ('0 products',  [],             5,       set()),
    ('1 product',   [F5],           5,       set()),
    ('no pair',     [F1,F5,F2,F6],  9,       set()),
    ('1 pair',      [F1,F5,F2,F6],  3,       {(F1,F2)}),
    ('2 pairs',     [F1,F5,F2,F6],  7,       {(F1,F6), (F5, F2)}),
    ('same price',  [F1,F5,F2,T5],  10,      {(F5,F5), (F5,T5), (T5,T5)})
]

test(pairs, pairs_tests)

### 9.3.1 Algorithm and complexity

#### Exercise 9.3.1

#### Exercise 9.3.2

#### Exercise 9.3.3

### 9.3.2 Code and tests

#### Exercise 9.3.4

#### Exercise 9.3.5