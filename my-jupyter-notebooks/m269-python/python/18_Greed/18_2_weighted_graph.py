# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 18.2 Weighted graphs

### 18.2.1 Data structures

### 18.2.2 Classes

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph

# CELL 2

# this code is also in m269_digraph.py

import math

class WeightedDiGraph(DiGraph):
    """A weighted directed graph with hashable node objects.

    Edges are between different nodes.
    There's at most one edge from one node to another.
    Edges have weights, which can be floats or integers.
    """

    def add_node(self, node: Hashable) -> None:
        """Add the node to the graph.

        Preconditions: not self.has_node(node)
        """
        self.out[node] = dict() # a map of out-neighbours to weights

    def add_edge(self, start: Hashable, end: Hashable, weight: float) -> None:
        """Add edge start -> end, with the given weight, to the graph.

        If the edge already exists, set its weight.

        Preconditions:
        self.has_node(start) and self.has_node(end) and start != end
        """
        self.out[start][end] = weight

    def weight(self, start: Hashable, end: Hashable) -> float:
        """Return the weight of edge start -> end or infinity if it doesn't exist.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        if self.has_edge(start, end):
            return self.out[start][end]
        else:
            return math.inf

    def remove_edge(self, start: Hashable, end: Hashable) -> None:
        """Remove edge start -> end from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(start) and self.has_node(end)
        """
        if self.has_edge(start, end):
            self.out[start].pop(end)

    def edges(self) -> set:
        """Return the graph's edges as a set of triples (start, end, weight)."""
        all_edges = set()
        for start in self.out:
            for (end, weight) in self.out[start].items():
                all_edges.add( (start, end, weight) )
        return all_edges

    def out_neighbours(self, node: Hashable) -> set:
        """Return the out-neighbours of the node.

        Preconditions: self.has_node(node)
        """
        return set(self.out[node].keys())

    def draw(self) -> None:
        """Draw the graph."""
        if type(self) == WeightedDiGraph:
            graph = networkx.DiGraph()
        else:
            graph = networkx.Graph()
        graph.add_nodes_from(self.nodes())
        for (node1, node2, weight) in self.edges():
            graph.add_edge(node1, node2, w=weight)
        pos = networkx.spring_layout(graph)
        networkx.draw(graph, pos, with_labels=True,
            node_size=1000, node_color='lightblue',
            font_size=12, font_weight='bold')
        networkx.draw_networkx_edge_labels(graph, pos,
            edge_labels=networkx.get_edge_attributes(graph, 'w'))

# CELL 3

graph = WeightedDiGraph()
for node in range(5):
    graph.add_node(node)
for node in range(5):
    graph.add_edge(node, (node + 1) % 5, node / 2)
graph.draw()

# CELL 4

# this code is also in m269_ungraph.py

class WeightedUndirectedGraph(WeightedDiGraph):
    """A weighted undirected graph with hashable node objects.

    There's at most one edge between two different nodes.
    There are no edges between a node and itself.
    Edges have weights, which may be integers or floats.
    """

    def add_edge(self, node1: Hashable, node2: Hashable, weight: float) -> None:
        """Add an edge node1-node2 with the given weight to the graph.

        If the edge already exists, set its weight.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().add_edge(node1, node2, weight)
        super().add_edge(node2, node1, weight)

    def remove_edge(self, node1: Hashable, node2: Hashable) -> None:
        """Remove edge node1-node2 from the graph.

        If the edge doesn't exist, do nothing.

        Preconditions: self.has_node(node1) and self.has_node(node2)
        """
        super().remove_edge(node1, node2)
        super().remove_edge(node2, node1)

    def edges(self) -> set:
        """Return the graph's edges as a set of triples (node1, node2, weight).

        Postconditions: for every edge A-B,
        the output has either (A, B, w) or (B, A, w) but not both
        """
        all_edges = set()
        for start in self.out:
            for (end, weight) in self.out[start].items():
                if (end, start, weight) not in all_edges:
                    all_edges.add( (start, end, weight) )
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