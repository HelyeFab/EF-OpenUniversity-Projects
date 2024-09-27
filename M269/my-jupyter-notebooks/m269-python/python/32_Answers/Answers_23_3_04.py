# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 23.3.4 answer

# CELL 1

def knapsack_bottomup(items: list, capacity: int) -> list:
    cache = []
    for index in range(len(items) + 1):
        cache.append([None] * (capacity + 1))

    for index in range(len(items), -1, -1):
        for c in range(capacity + 1):
            if index == len(items) or c == 0:
                cache[index][c] = []
            else:
                item = items[index]
                skip = cache[index + 1][c]
                if item[WEIGHT] > c:
                    cache[index][c] = skip
                else:
                    take = [item] + cache[index+1][c - item[WEIGHT]]
                    if value(skip) > value(take):
                        cache[index][c] = skip
                    else:
                        cache[index][c] = take

    return cache[0][capacity]