# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 21.3 Topological sort

### 21.3.1 Problem

# CELL 1

# %run -i ../m269_digraph

spreadsheet = DiGraph()
for node in ('A2', 'B2', 'C2'):
    spreadsheet.add_node(node)
spreadsheet.add_edge('A2', 'B2')
spreadsheet.add_edge('A2', 'C2')
spreadsheet.add_edge('B2', 'C2')

### 21.3.2 Algorithm and code

# CELL 2

# %run -i ../m269_stack

# CELL 3

# this code is also in m269_digraph.py

def topological_sort(graph: DiGraph) -> list:
    """Return a topological sort of graph.

    Preconditions: graph is acyclic
    Postconditions:
    - the output is a permutation of the graph's nodes
    - for every edge A -> B, node A appears before B in the output
    """
    schedule = []

    # compute the initial in-degrees
    indegree = dict()
    for node in graph.nodes():
        indegree[node] = 0
    for edge in graph.edges():
        indegree[edge[1]] = indegree[edge[1]] + 1

    # compute the nodes that can be visited first
    to_visit = Stack()
    for node in graph.nodes():
        if indegree[node] == 0:
            to_visit.push(node)

    while to_visit.size() > 0:
        visited = to_visit.pop()
        schedule.append(visited)
        # simulate the removal of the visited node
        for neighbour in graph.neighbours(visited):
            indegree[neighbour] = indegree[neighbour] - 1
            if indegree[neighbour] == 0:
                to_visit.push(neighbour)
    return schedule

# CELL 4

topological_sort(spreadsheet)

### 21.3.3 Complexity

### 21.3.4 Exercises

#### Exercise 21.3.1

#### Exercise 21.3.2

#### Exercise 21.3.3

# CELL 5

from algoesup import test

def is_cyclic(graph: DiGraph) -> bool:
    """Return True if and only if the graph has a cycle."""
    pass

digraph = DiGraph()                     # from Section 21.2.1
for node in 'ABCDEF':
    digraph.add_node(node)
for edge in ('AB', 'BC', 'CA', 'DE'):   # cycle A -> B -> C -> A
    digraph.add_edge(edge[0], edge[1])

is_cyclic_tests = [
    # case,         graph,          is cyclic?
    ('has cycle',   digraph,        True),
    ('no cycle',    spreadsheet,    False)
]

test(is_cyclic, is_cyclic_tests)

#### Exercise 21.3.4