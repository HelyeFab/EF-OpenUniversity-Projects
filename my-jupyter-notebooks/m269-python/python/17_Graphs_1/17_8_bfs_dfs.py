# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 17.8 Breadth- and depth-first search

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph
# %run -i ../m269_graphs

### 17.8.1 Breadth-first search

# CELL 2

# %run -i ../m269_queue.py

# CELL 3

# this code is also in m269_digraph.py

def bfs(graph: DiGraph, start: Hashable) -> DiGraph:
    """Return the subgraph traversed by a breadth-first search.

    Preconditions: graph.has_node(start)
    """
    # changes from traversed function noted in comments
    visited = DiGraph()
    visited.add_node(start)
    unprocessed = Queue()                                   # was set
    for neighbour in graph.out_neighbours(start):
        unprocessed.enqueue( (start, neighbour) )           # was add()
    while unprocessed.size() > 0:                           # was len()
        edge = unprocessed.dequeue()                        # was pop()
        previous = edge[0]
        current = edge[1]
        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current)
            for neighbour in graph.out_neighbours(current):
                unprocessed.enqueue( (current, neighbour) ) # was add()
    return visited

### 17.8.2 Depth-first search

# CELL 4

# %run -i ../m269_stack

# CELL 5

# this code is also in m269_digraph.py

def dfs(graph: DiGraph, start: Hashable) -> DiGraph:
    """Return the subgraph traversed by a depth-first search.

    Preconditions: graph.has_node(start)
    """
    visited = DiGraph()
    visited.add_node(start)
    unprocessed = Stack()                                   # was Queue()
    for neighbour in graph.out_neighbours(start):
        unprocessed.push( (start, neighbour) )              # was enqueue()
    while unprocessed.size() > 0:
        edge = unprocessed.pop()                            # was dequeue()
        previous = edge[0]
        current = edge[1]
        if not visited.has_node(current):
            visited.add_node(current)
            visited.add_edge(previous, current)
            for neighbour in graph.out_neighbours(current):
                unprocessed.push( (current, neighbour) )    # was enqueue()
    return visited

### 17.8.3 Tests

# CELL 6

bfs(null_graph(3), 0).draw()        # nodes: 0, 1, 2; start node: 0

# CELL 7

dfs(null_graph(3), 0).draw()

# CELL 8

bfs(path_graph(4), 1).draw()        # start node: 1

# CELL 9

dfs(path_graph(4), 1).draw()

# CELL 10

bfs(complete_graph(4), 2).draw()    # start node: 2

# CELL 11

dfs(complete_graph(4), 2).draw()

# CELL 12

random = random_graph(6, 0.4)   # set a lower or higher probability
random.draw()

# CELL 13

bfs(random, 3).draw()           # start node: 3

# CELL 14

dfs(random, 3).draw()

### 17.8.4 Comparison

# CELL 15

kite = DiGraph()
for node in 'ABCD':
    kite.add_node(node)
for edge in ('AB', 'AC', 'BD', 'CD'):
    kite.add_edge(edge[0], edge[1])
kite.draw()

# CELL 16

bfs(kite, 'A').draw()