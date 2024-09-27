# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 21.3.3 answer

# CELL 1

# %run -i ../m269_digraph

def is_cyclic(graph: DiGraph) -> bool:
    """Return True if and only if the graph has a cycle."""
    return len(topological_sort(graph)) < len(graph.nodes())