# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 21.1.1 answer

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph
# %run -i ../m269_queue
# %run -i ../m269_stack

def disconnected(graph: UndirectedGraph, sources: set) -> set:
    """Return all nodes not connected to any of the sources.

    Preconditions: sources is a non-empty subset of the graph's nodes
    """
    connected = set()
    for source in sources:
        if source not in connected:
            reached = bfs(graph, source).nodes()
            connected = connected.union(reached)
    return graph.nodes() - connected