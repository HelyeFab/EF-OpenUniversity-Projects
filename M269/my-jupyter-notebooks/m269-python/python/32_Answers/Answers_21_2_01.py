# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 21.2.1 answer

# CELL 1

# %run -i ../m269_digraph.py
# %run -i ../m269_ungraph.py
# %run -i ../m269_queue
# %run -i ../m269_stack

def weakly_connected_components(graph: DiGraph) -> dict:
    """Return the weakly connected components of graph.

    Postconditions: the output maps each node to its component,
    numbered from 1 onwards.
    """
    undirected = UndirectedGraph()
    for node in graph.nodes():
        undirected.add_node(node)
    for edge in graph.edges():
        undirected.add_edge(edge[0], edge[1])
    return connected_components(undirected)