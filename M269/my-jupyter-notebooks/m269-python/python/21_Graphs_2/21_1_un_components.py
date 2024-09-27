# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 21.1 Undirected graph components

### 21.1.1 Problem definition and instances

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph
# %run -i ../m269_queue
# %run -i ../m269_stack

# CELL 2

undirected = UndirectedGraph()
for node in 'ABCDEF':
    undirected.add_node(node)
undirected.add_edge('A', 'B')
undirected.add_edge('A', 'C')
undirected.add_edge('D', 'E')

### 21.1.2 Algorithm and complexity

### 21.1.3 Code and tests

# CELL 3

# this code is also in m269_ungraph.py

def connected_components(graph: UndirectedGraph) -> dict:
    """Return the connected components of graph.

    Postconditions: the output maps each node to its component,
    numbered from 1 onwards.
    """
    component = dict()
    counter = 1
    for node in graph.nodes():
        if node not in component:
            tree = dfs(graph, node)
            for reached in tree.nodes():
                component[reached] = counter
            counter = counter + 1
    return component

# CELL 4

connected_components(undirected)

# CELL 5

# %run -i ../m269_graphs

# most components: no node has neighbours
connected_components(null_graph(5))

# CELL 6

# fewest components: a connected graph; could be cycle graph or complete graph
connected_components(path_graph(5))

#### Exercise 21.1.1

# CELL 7

def disconnected(graph: UndirectedGraph, sources: set) -> set:
    """Return all nodes not connected to any of the sources.

    Preconditions: sources is a non-empty subset of the graph's nodes
    """
    pass

disconnected(undirected, {'A'})     # you should obtain {'D', 'E', 'F'}

#### Exercise 21.1.2