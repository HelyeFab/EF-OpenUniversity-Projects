# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 17.7 Traversing a graph

### 17.7.1 First algorithm

### 17.7.2 Complexity

### 17.7.3 Code and tests

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph
# %run -i ../m269_graphs

# CELL 2

def traversal(graph: DiGraph, start: Hashable) -> list:
    """Return all nodes reachable from start, in the order visited.

    Preconditions: graph.has_node(start)
    """
    visited = [start]
    unprocessed = graph.out_neighbours(start)
    while len(unprocessed) > 0:
        node = unprocessed.pop()
        if node not in visited:
            visited.append(node)
            for neighbour in graph.out_neighbours(node):
                unprocessed.add(neighbour)
    return visited

# CELL 3

traversal(null_graph(3), 0)    # null graph with several nodes

# CELL 4

traversal(path_graph(4), 1)    # start from node 1

# CELL 5

traversal(complete_graph(4), 0)

#### Exercise 17.7.1

### 17.7.4 Second algorithm

# CELL 6

def traversed(graph: DiGraph, start: Hashable) -> DiGraph:
    """Return the traversed subgraph when beginning at start.

    Preconditions: graph.has_node(start)
    """
    visited = DiGraph()
    visited.add_node(start)
    unprocessed = set()
    for neighbour in graph.out_neighbours(start):
        unprocessed.add( (start, neighbour) )
    while len(unprocessed) > 0:
        edge = unprocessed.pop()
        previous = edge[0]
        current = edge[1]
        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current)
            for neighbour in graph.out_neighbours(current):
                unprocessed.add( (current, neighbour) )
    return visited

# CELL 7

traversed(null_graph(3), 0).draw()  # null graph with several nodes

# CELL 8

traversed(path_graph(4), 1).draw()  # start from node 1

# CELL 9

traversed(complete_graph(4), 0).draw()

# CELL 10

random = random_graph(6, 0.4)
random.draw()

# CELL 11

traversed(random, 3).draw()         # start from node 3

# CELL 12

traversed(random, 5).draw()         # start from node 5

#### Exercise 17.7.2