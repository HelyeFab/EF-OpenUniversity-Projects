# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 23.3.3 answer

# CELL 1

def knapsack_topdown(items: list, capacity: int) -> list:
    def knapsack(index: int, capacity: int) -> list:
        """Return a subsequence of items[index:] that
        fits the capacity and maximises the value.

        Preconditions: 0 ≤ index ≤ len(items) and 0 ≤ capacity
        """
        if cache[index][capacity] == None:
            if index == len(items) or capacity == 0:
                cache[index][capacity] = []
            else:
                item = items[index]
                skip = knapsack(index + 1, capacity)
                if item[WEIGHT] > capacity:
                    cache[index][capacity] = skip
                else:
                    take = [item] + knapsack(index + 1, capacity - item[WEIGHT])
                    if value(skip) > value(take):
                        cache[index][capacity] = skip
                    else:
                        cache[index][capacity] = take
            print('cache[', index, '][', capacity, '] =', cache[index][capacity])
        return cache[index][capacity]

    cache = []
    for index in range(len(items) + 1):
        cache.append([None] * (capacity + 1))
    return knapsack(0, capacity)