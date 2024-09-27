# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 23.3.1 answer

# CELL 1

def knapsack_indices(items: list, capacity: int) -> list:
    # docstring not repeated

    def knapsack(index: int, capacity: int) -> list:
        """Return a subsequence of items[index:] that
        fits the capacity and maximises the value.

        Preconditions: 0 ≤ index ≤ len(items) and 0 ≤ capacity
        """
        if index == len(items) or capacity == 0:
            return []
        else:
            item = items[index]
            skip = knapsack(index + 1, capacity)
            if item[WEIGHT] > capacity:
                return skip
            else:
                take = [item] + knapsack(index + 1, capacity - item[WEIGHT])
                if value(skip) > value(take):
                    return skip
                else:
                    return take

    return knapsack(0, capacity)