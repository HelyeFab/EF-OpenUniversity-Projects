# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 18.3 Minimum spanning tree

### 18.3.1 First algorithm

#### Exercise 18.3.1

#### Exercise 18.3.2

### 18.3.2 Second algorithm

#### Exercise 18.3.3

#### Exercise 18.3.4

### 18.3.3 Code

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph

# CELL 2

# this code is also in m269_ungraph.py

from heapq import heappush, heappop

def prim(graph: WeightedUndirectedGraph, start: Hashable) -> WeightedUndirectedGraph:
    """Return a minimum spanning tree of graph, beginning at start.

    Preconditions:
    - graph.has_node(start)
    - graph is connected
    - node objects are comparable
    """
    visited = WeightedUndirectedGraph()
    visited.add_node(start)

    unprocessed = []
    for neighbour in graph.neighbours(start):
        weight = graph.weight(start, neighbour)
        heappush(unprocessed, (weight, start, neighbour) )

    while len(unprocessed) > 0:
        edge = heappop(unprocessed)
        weight = edge[0]
        previous = edge[1]
        current = edge[2]
        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current, weight)
            for neighbour in graph.neighbours(current):
                weight = graph.weight(current, neighbour)
                heappush(unprocessed, (weight, current, neighbour) )
    return visited

# CELL 3

# this code is also in m269_graphs.py

# graph in Figure 18.3.1
RHOMBUS = WeightedUndirectedGraph()
for node in 'ABCD':
    RHOMBUS.add_node(node)
RHOMBUS.add_edge('A', 'B', 1)
RHOMBUS.add_edge('A', 'D', 2)
RHOMBUS.add_edge('B', 'C', 4)
RHOMBUS.add_edge('B', 'D', 2)
RHOMBUS.add_edge('C', 'D', 5)

# CELL 4

RHOMBUS.draw()

# CELL 5

prim(RHOMBUS, 'D').draw()  # replace D with A, B or C