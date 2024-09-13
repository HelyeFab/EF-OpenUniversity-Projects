# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 19.3.5 answer

# CELL 1

# %run -i ../m269_digraph
# %run -i ../m269_ungraph
# %run -i ../m269_graphs
from algoesup import test

def weak_points(beams: set) -> set:
    """Return the points that aren't part of any triangle.

    beams is a set of pairs of integers.
    The output is a set of integers.
    Each integer represents a point.

    Preconditions: for every pair (a, b), a ≠ b
    Postconditions: the output only has points occurring in beams
    """
    def is_weak(point: int, structure: UndirectedGraph) -> bool:
        """Return True if point isn't part of a triangle in structure."""
        neighbours = structure.neighbours(point)
        for point2 in neighbours:
            for point3 in neighbours:
                if structure.has_edge(point2, point3):
                    return False
        return True

    structure = UndirectedGraph()
    for beam in beams:
        if not structure.has_node(beam[0]):
            structure.add_node(beam[0])
        if not structure.has_node(beam[1]):
            structure.add_node(beam[1])
        structure.add_edge(beam[0], beam[1])

    weak = set()
    for point in structure.nodes():
        if is_weak(point, structure):
            weak.add(point)
    return weak

T134 = {(1,3), (1,4), (3,4)}    # some triangles
T346 = {(3,4), (4,6), (6,3)}
worst = complete_graph(5)       # complete graphs are a worst case

weak_points_tests = [
    # case,             beams,                      weak points
    ('no triangle',     {(1,2), (3,1)},             {1, 2, 3}),
    ('missing points',  {(7,3), (3,2)},             {2, 3, 7}),
    # your tests:
    ('no points',       {},                         set()),
    ('mixed points',    T134|T346|{(2,1), (6,9)},   {2, 9}),
    ('best case',       {(1,3), (5,2)},             {1, 2, 3, 5}),
    ('worst case',      worst.edges(),              set())
]

test(weak_points, weak_points_tests)