# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 18.4 Shortest paths

### 18.4.1 Algorithm

#### Exercise 18.4.1

### 18.4.2 Code

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph
# %run -i ../m269_graphs

# CELL 2

# this code is also in m269_digraph.py

from heapq import heappush, heappop

def dijkstra(graph: WeightedDiGraph, start: Hashable) -> WeightedDiGraph:
    """Return a shortest path from start to each reachable node.

    Preconditions:
    - graph.has_node(start)
    - node objects are comparable
    - no weight is negative
    """
    visited = WeightedDiGraph()
    visited.add_node(start)

    # create min-priority queue of tuples (cost, (A, B, weight))
    # cost is total weight from start to B via shortest path to A
    unprocessed = []    # min-priority queue
    for neighbour in graph.out_neighbours(start):
        weight = graph.weight(start, neighbour)
        heappush(unprocessed, (weight, (start, neighbour, weight)) )

    while len(unprocessed) > 0:
        info = heappop(unprocessed)
        cost = info[0]
        edge = info[1]
        previous = edge[0]
        current = edge[1]
        weight = edge[2]

        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current, weight)
            for neighbour in graph.out_neighbours(current):
                weight = graph.weight(current, neighbour)
                edge = (current, neighbour, weight)
                heappush(unprocessed, (cost + weight, edge) )
    return visited

# CELL 3

RHOMBUS.draw()

# CELL 4

dijkstra(RHOMBUS, 'A').draw()

# CELL 5

dijkstra(RHOMBUS, 'D').draw()

# CELL 6

# this code is also in m269_graphs.py

# graph used by the interactive visualisation of Dijkstra's algorithm
DIJKSTRA = WeightedUndirectedGraph()
for node in 'ABCDEFGHK':
    DIJKSTRA.add_node(node)
DIJKSTRA.add_edge('C', 'A', 20)
DIJKSTRA.add_edge('A', 'B', 4)
DIJKSTRA.add_edge('B', 'F', 1)
DIJKSTRA.add_edge('F', 'H', 1)
DIJKSTRA.add_edge('B', 'G', 3)
DIJKSTRA.add_edge('G', 'K', 5)
DIJKSTRA.add_edge('K', 'H', 3)
DIJKSTRA.add_edge('C', 'D', 2)
DIJKSTRA.add_edge('D', 'E', 2)
DIJKSTRA.add_edge('E', 'G', 3)
DIJKSTRA.add_edge('E', 'K', 3)

# CELL 7

DIJKSTRA.draw()

# CELL 8

prim(DIJKSTRA, 'C').draw()

# CELL 9

# the automated layout of graphs is semi-random
# you may need to re-run this cell several times to get a good layout
dijkstra(DIJKSTRA, 'C').draw()

### 18.4.3 Applications

#### Exercise 18.4.2

#### Exercise 18.4.3