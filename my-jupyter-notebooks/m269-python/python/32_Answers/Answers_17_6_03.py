# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 17.6.3 answer

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph

def same_degree(graph: UndirectedGraph) -> bool:
    """Return True if and only if all nodes have the same degree.

    Preconditions: graph isn't empty
    """
    all_degrees = set()
    for node in graph.nodes():
        all_degrees.add(graph.degree(node))
    return len(all_degrees) == 1