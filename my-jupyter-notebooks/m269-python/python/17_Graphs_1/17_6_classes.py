# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 17.6 Classes for graphs

### 17.6.1 The `DiGraph` class

# CELL 1

# this code is also in m269_digraph.py

import networkx
from typing import Hashable

class DiGraph:
    """A directed graph with hashable node objects.

    Edges are between different nodes.
    There's at most one edge from one node to another.
    """

    def __init__(self):
        self.out = dict()   # a map of nodes to their out-neighbours

    def has_node(self, node: Hashable) -> bool:
        """Return True if and only if the graph has the node."""
        return node in self.out

    def has_edge(self, start: Hashable, end: Hashable) -> bool:
        """Return True if and only if edge start -> end exists.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        return end in self.out[start]

    def add_node(self, node: Hashable) -> None:
        """Add the node to the graph.

        Preconditions: not self.has_node(node)
        """
        self.out[node] = set()

    def add_edge(self, start: Hashable, end: Hashable) -> None:
        """Add edge start -> end to the graph.

        If the edge already exists, do nothing.

        Preconditions:
        self.has_node(start) and self.has_node(end) and start != end
        """
        self.out[start].add(end)

    def remove_node(self, node: Hashable) -> None:
        """Remove the node and all its attached edges.

        Preconditions: self.has_node(node)
        """
        for start in self.out:
            self.remove_edge(start, node)
        self.out.pop(node)

    def remove_edge(self, start: Hashable, end: Hashable) -> None:
        """Remove edge start -> end from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        self.out[start].discard(end)

    def nodes(self) -> set:
        """Return the graph's nodes."""
        all_nodes = set()
        for node in self.out:
            all_nodes.add(node)
        return all_nodes

    def edges(self) -> set:
        """Return the graph's edges as a set of pairs (start, end)."""
        all_edges = set()
        for start in self.out:
            for end in self.out[start]:
                all_edges.add( (start, end) )
        return all_edges

    def out_neighbours(self, node: Hashable) -> set:
        """Return the out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return set(self.out[node])  # return a copy

    def out_degree(self, node: Hashable) -> int:
        """Return the number of out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return len(self.out[node])

    def in_neighbours(self, node: Hashable) -> set:
        """Return the in-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        start_nodes = set()
        for start in self.out:
            if self.has_edge(start, node):
                start_nodes.add(start)
        return start_nodes

    def in_degree(self, node: Hashable) -> int:
        """Return the number of in-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return len(self.in_neighbours(node))

    def neighbours(self, node: Hashable) -> set:
        """Return the in- and out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node).union(self.in_neighbours(node))

    def degree(self, node: Hashable) -> int:
        """Return the number of in- and out-going edges of the node.

        Preconditions: self.has_node(node)
        """
        return self.in_degree(node) + self.out_degree(node)

    def draw(self) -> None:
        """Draw the graph."""
        if type(self) == DiGraph:
            graph = networkx.DiGraph()
        else:
            graph = networkx.Graph()
        graph.add_nodes_from(self.nodes())
        graph.add_edges_from(self.edges())
        networkx.draw(graph, with_labels=True,
            node_size=1000, node_color='lightblue',
            font_size=12, font_weight='bold')

#### Exercise 17.6.1 (optional)

### 17.6.2 The `UndirectedGraph` class

# CELL 2

# this code is also in m269_ungraph.py

from typing import Hashable

class UndirectedGraph(DiGraph):
    """An undirected graph with hashable node objects.

    There's at most one edge between two different nodes.
    There are no edges between a node and itself.
    """

    def add_edge(self, node1: Hashable, node2: Hashable) -> None:
        """Add an undirected edge node1-node2 to the graph.

        If the edge already exists, do nothing.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().add_edge(node1, node2)
        super().add_edge(node2, node1)

    def remove_edge(self, node1: Hashable, node2: Hashable) -> None:
        """Remove edge node1-node2 from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().remove_edge(node1, node2)
        super().remove_edge(node2, node1)

    def edges(self) -> set:
        """Return the graph's edges as a set of pairs.

        Postconditions: for every edge A-B,
        the output has either (A, B) or (B, A) but not both
        """
        all_edges = set()
        for node1 in self.out:
            for node2 in self.out[node1]:
                if (node2, node1) not in all_edges:
                    all_edges.add( (node1, node2) )
        return all_edges

    def in_neighbours(self, node: Hashable) -> set:
        """Return all nodes that are adjacent to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node)

    def neighbours(self, node: Hashable) -> set:
        """Return all nodes that are adjacent to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_neighbours(node)

    def in_degree(self, node: Hashable) -> int:
        """Return the number of edges attached to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_degree(node)

    def degree(self, node: Hashable) -> int:
        """Return the number of edges attached to the node.

        Preconditions: self.has_node(node)
        """
        return self.out_degree(node)

#### Exercise 17.6.2 (optional)

### 17.6.3 Special graphs

# CELL 3

# this code is also in m269_graphs.py

EMPTY = UndirectedGraph()

def null_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, 1, ..., n-1 and no edges.

    Preconditions: n > 0
    """
    graph = UndirectedGraph()
    for node in range(n):
        graph.add_node(node)
    return graph

def path_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, ..., n-1 and edges 0–1, 1–2, ....

    Preconditions: n > 0
    """
    graph = null_graph(n)
    for node in range(n-1):
        graph.add_edge(node, node+1)
    return graph

def cycle_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, ..., n-1 and edges 0–1, 1–2, ..., (n-1)–0.

    Preconditions: n > 0
    """
    graph = path_graph(n)
    graph.add_edge(n-1, 0)
    return graph

def complete_graph(n: int) -> UndirectedGraph:
    """Return a graph with nodes 0, ..., n-1 connected to each other.

    Preconditions: n > 0
    """
    graph = null_graph(n)
    for node1 in range(n):
        for node2 in range(node1 + 1, n):
            graph.add_edge(node1, node2)
    return graph

# CELL 4

# %matplotlib inline

# CELL 5

null_graph(1).draw()

# CELL 6

path_graph(2).draw()

# CELL 7

cycle_graph(3).draw()

# CELL 8

complete_graph(4).draw()

#### Exercise 17.6.3

# CELL 9

from algoesup import test

def same_degree(graph: UndirectedGraph) -> bool:
    """Return True if and only if all nodes have the same degree.

    Preconditions: graph isn't empty
    """
    pass

same_degree_tests = [
    #case,          graph,        same degree?
    ('null',        null_graph(1),      True),  # all have degree 0
    ('path 2',      path_graph(2),      True),  # all have degree 1
    ('path 3',      path_graph(3),     False),
    ('cycle',       cycle_graph(3),     True),  # all have degree 2
    ('complete',    complete_graph(4),  True)   # all have degree 3
]

test(same_degree, same_degree_tests)

### 17.6.4 Random graphs

# CELL 10

# this code is also in m269_graphs.py

from random import random

def random_graph(n: int, probability: float) -> UndirectedGraph:
    """Generate a random graph with n nodes.

    Each edge has the given probability of existing.
    Preconditions: 0 <= probability <= 1
    """
    graph = null_graph(n)
    for node1 in range(n):
        for node2 in range(node1 + 1, n):
            if random() < probability:
                graph.add_edge(node1, node2)
    return graph

# CELL 11

random_graph(6, 0).draw()   # p = 0%: no edges

# CELL 12

random_graph(6, 0.4).draw() # p = 40%

# CELL 13

random_graph(6, 0.4).draw() # different graph for same n and p

# CELL 14

random_graph(6, 1).draw()   # p = 100%: all edges