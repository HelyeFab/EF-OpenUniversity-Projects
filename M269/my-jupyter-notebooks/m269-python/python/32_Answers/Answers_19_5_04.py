# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 19.5.4 answer

# CELL 1

from algoesup import test
# %run -i ../m269_queue
# %run -i ../m269_digraph
# %run -i ../m269_ungraph

def knight_moves(size: tuple, start: tuple, end: tuple) -> int:
    """Return least number of knight moves from start to end.

    Return -1 if end is not reachable from start.

    Preconditions:
    - size is a pair (rows, columns) with rows > 0 and columns > 0
    - start and end are pairs (r, c) with 0 <= r < rows and 0 <= c < columns
    """
    def can_move(square1: tuple, square2: tuple) -> bool:
        """Check if a knight can move from one square to the other.

        Preconditions:
        the inputs are pairs (r, c) with 0 <= r < rows and 0 <= c < columns
        """
        vertical = abs(square1[0] - square2[0])   # movement between rows
        horizontal = abs(square1[1] - square2[1]) # movement between columns
        movement = (vertical, horizontal)
        return movement == (2, 1) or movement == (1, 2)

    if end == start:
        return 0

    graph = UndirectedGraph()
    for row in range(size[0]):
        for column in range(size[1]):
            graph.add_node( (row, column) )
    for node1 in graph.nodes():
        for node2 in graph.nodes():
            if can_move(node1, node2):
                graph.add_edge(node1, node2)

    visited = {start}
    unprocessed = Queue()
    for neighbour in graph.out_neighbours(start):
        unprocessed.enqueue( (start, neighbour, 1) )
    while unprocessed.size() > 0:
        edge = unprocessed.dequeue()
        previous = edge[0]
        current = edge[1]
        length = edge[2]
        if current == end:
            return length
        elif current not in visited:
            visited.add(current)
            for neighbour in graph.out_neighbours(current):
                unprocessed.enqueue( (current, neighbour, length+1) )
    return -1

knight_moves_tests = [
    # case,             size,   start,  end,    moves
    ('1x1 board',       (1, 1), (0, 0), (0, 0),     0),
    ('1 row, 2 cols',   (1, 2), (0, 0), (0, 1),    -1),
    ('2 rows, 1 col',   (2, 1), (1, 0), (0, 0),    -1),
    ('start = end',     (3, 3), (1, 1), (1, 1),     0),
    ('bottom left',     (5, 6), (3, 4), (4, 0),     3), # figure 19.5.1
    ('bottom right',    (5, 6), (3, 4), (4, 5),     4), # figure 19.5.1
    ('3x3 to centre',   (3, 3), (0, 0), (1, 1),    -1), # figure 19.5.2
]

test(knight_moves, knight_moves_tests)