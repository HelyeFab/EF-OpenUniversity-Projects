# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 11.4 Searching permutations

### 11.4.1 Problem

### 11.4.2 Algorithm

#### Exercise 11.4.1

### 11.4.3 Complexity

# CELL 1

from math import factorial

print(factorial(15), 'µs')

# CELL 2

MS_PER_DAY = 24 * 60 * 60 * 1000 * 1000     # microseconds in a day
print(factorial(15) //  MS_PER_DAY, 'days')

# CELL 3

MS_PER_S = 1000 ** 2    # microseconds in a second
print(factorial(10) // MS_PER_S, 'seconds')

#### Exercise 11.4.2

### 11.4.4 Code

# CELL 4

from itertools import permutations

for permutation in permutations({'travelling', 'salesman', 'problem'}):
    print(permutation)

# CELL 5

four_places = [
    [0, 15, 10, 5],     # cost from 0 to other places
    [15, 0, 30, 5],     # cost from 1 to other places
    [10, 30, 0, 10],    # cost from 2 to other places
    [5, 5, 10, 0],      # cost from 3 to other places
]

# CELL 6

from itertools import permutations
import math

def tsp(costs: list) -> tuple:
    """Solve the travelling salesman problem.

    Input: costs is a n*n matrix of numbers
    Preconditions:
    - n > 1
    - costs[i][j] is the cost of travelling from i to j
    Postconditions:
    - len(output) = n + 1
    - output[0] = output[n]
    - every integer from 0 to n - 1 occurs in the output
    - costs[output[0]][output[1]] + ... + costs[output[n-1]][output[n]]
      has the lowest possible value
    """
    best_cost = math.inf    # positive infinity (Section 6.8)
    n = len(costs)
    # generate all permutations of (1, .., n-1)
    for places in permutations(range(1, n)):
        # tuple literals with 1 item need extra comma (Section 4.5)
        tour = (0,) + places + (0,)
        cost = 0
        for index in range(0, n):
            cost = cost + costs[tour[index]][tour[index+1]]
        if cost < best_cost:
            best_cost = cost
            best_tour = tour
    return best_tour

tsp(four_places)