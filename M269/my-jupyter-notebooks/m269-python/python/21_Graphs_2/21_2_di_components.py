# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 21.2 Directed graph components

### 21.2.1 Problem and instances

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_queue
# %run -i ../m269_stack

digraph = DiGraph()
for node in 'ABCDEF':
    digraph.add_node(node)
for edge in ('AB', 'BC', 'CA', 'DE'):
    digraph.add_edge(edge[0], edge[1])

#### Exercise 21.2.1

# CELL 2

def weakly_connected_components(graph: DiGraph) -> dict:
    """Return the weakly connected components of graph.

    Postconditions: the output maps each node to its component,
    numbered from 1 onwards.
    """
    pass

weakly_connected_components(digraph)

### 21.2.2 Algorithm and complexity

### 21.2.3 Code and tests

# CELL 3

# this code is also in m269_digraph.py

def reverse(graph: DiGraph) -> DiGraph:
    """Return the same graph but with edge directions reversed."""
    reversed = DiGraph()
    for node in graph.nodes():
        reversed.add_node(node)
    for edge in graph.edges():
        reversed.add_edge(edge[1], edge[0])
    return reversed

def strongly_connected_components(graph: DiGraph) -> dict:
    """Return the strongly connected components of graph.

    Postconditions: the output maps each node to its component,
    numbered from 1 onwards.
    """
    reversed = reverse(graph)
    component = dict()
    counter = 1
    for node in graph.nodes():
        if node not in component:
            forward = dfs(graph, node).nodes()
            backward = dfs(reversed, node).nodes()
            for common in forward.intersection(backward):
                component[common] = counter
            counter = counter + 1
    return component

# CELL 4

strongly_connected_components(digraph)