# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 22.5 Back to the TSP

# CELL 1

import math
# %run -i ../m269_digraph.py     # (un)weighted directed graph classes
# %run -i ../m269_ungraph.py     # undirected graph classes inherit from directed

example = WeightedUndirectedGraph()
for node in range(5):
    example.add_node(node)
example.add_edge(0, 1, 20)
example.add_edge(0, 2, math.inf)
example.add_edge(0, 3, 10)
example.add_edge(0, 4, 5)
example.add_edge(1, 2, 10)
example.add_edge(1, 3, 5)
example.add_edge(1, 4, math.inf)
example.add_edge(2, 3, 10)
example.add_edge(2, 4, 20)
example.add_edge(3, 4, 10)

### 22.5.1 The main function

# CELL 2

SOLUTION = 0
VALUE = 1

def tsp(graph: WeightedUndirectedGraph) -> list:
    """Return a tour-length pair with shortest length.

    Preconditions:
    graph is complete, has nodes 0, 1, ..., and positive weights
    Postconditions: tour starts and ends at node 0
    """
    path = [0]
    nodes = graph.nodes()
    solution = []
    shortest = [solution, math.inf]
    extend(path, nodes, graph, shortest)
    return shortest[SOLUTION]

### 22.5.2 The value function

# CELL 3

# help(WeightedUndirectedGraph)

#### Exercise 22.5.1

# CELL 4

def value(candidate: list, instance: object) -> int:
    """Return the value of the candidate sequence for the problem instance."""
    pass # replace with your code

value([0, 1, 2, 3, 4, 0], example) == 55

### 22.5.3 Checking the constraints

#### Exercise 22.5.2

# CELL 5

def satisfies_global(candidate: list, instance: object) -> bool:
    """Check if the candidate satisfies the global constraints."""
    pass # replace with your code

#### Exercise 22.5.3

# CELL 6

def can_extend(item: object, candidate: list, instance: object, best: list) -> bool:
    """Check if item can extend candidate into a better solution than best."""
    # replace ... with a check for the local constraints
    # use < for a minimisation problem
    return ... and value(candidate + [item]) > best[VALUE]

### 22.5.4 The backtracking function

#### Exercise 22.5.4

# CELL 7

def extend(candidate: list, extensions: set, instance: object, best: list) -> None:
    """Update best if candidate is a better solution, otherwise extend it."""
    print('Visiting node', candidate, extensions)
    # remove the next line if partial candidates can be solutions
    if len(extensions) == 0:
        if satisfies_global(candidate, instance):
            candidate_value = value(candidate, instance)
            # in the next line, use < for minimisation problems
            if candidate_value > best[VALUE]:
                print('New best with value', candidate_value)
                best[SOLUTION] = candidate
                best[VALUE] = candidate_value
    for item in extensions:
        if can_extend(item, candidate, instance, best):
            extend(candidate + [item], extensions - {item}, instance, best)

# CELL 8

# tsp(example) in [ [0,3,1,2,4,0], [0,4,2,1,3,0] ]

#### Exercise 22.5.5