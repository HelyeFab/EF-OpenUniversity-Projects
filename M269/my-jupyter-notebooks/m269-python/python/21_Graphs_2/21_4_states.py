# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 21.4 State graphs

### 21.4.1 Problem

# CELL 1

rook_moves_tests = [
    # case,             size,   start,  end,    moves
    ('1x1 board',       (1, 1), (0, 0), (0, 0),     0),
    ('1 row, 2 cols',   (1, 2), (0, 0), (0, 1),     1),
    ('start = end',     (3, 3), (1, 1), (1, 1),     0),
    ('figure example',  (4, 4), (0, 0), (3, 2),     4),
    ('2 away',          (4, 4), (0, 0), (0, 2),    -1)
]

### 21.4.2 Graph

### 21.4.3 Code

# CELL 2

# %run -i ../m269_digraph

def state_transitions(size: tuple) -> DiGraph:
    """Return the state transition graph for a board of the given size.

    Preconditions: size is a pair of positive integers, the number of rows and columns
    """
    rows = size[0]
    columns = size[1]
    states = DiGraph()
    # add nodes (S, 1), (S, 2), (S, 3) for every square S
    for row in range(rows):
        for column in range(columns):
            for move in (1, 2, 3):
                states.add_node( ((row, column), move) )
    # add edges
    for state in states.nodes():
        position = state[0]
        distance = state[1]

        row = position[0]
        column = position[1]

        next_distance = distance % 3 + 1    # 1 -> 2 -> 3 -> 1 -> ...

        # generate the 4 possible moves: up, left, down, right
        for move in (-distance, distance):
            # do vertical move if it stays within board
            if 0 <= row + move < rows:
                next_state = ( (row+move, column), next_distance)
                states.add_edge(state, next_state)
            # do horizontal move if it stays within board
            if 0 <= column + move < columns:
                next_state = ( (row, column+move), next_distance)
                states.add_edge(state, next_state)

    return states

# CELL 3

state_transitions( (1, 3) ).draw()    # single row, three columns

# CELL 4

# %run -i ../m269_queue

def rook_moves(size: tuple, start: tuple, end: tuple) -> int:
    """Return the least number of 1, 2, 3, 1, ... rook moves from start to end.

    Return -1 if end is not reachable from start.

    Preconditions:
    - size is a pair (rows, columns) with rows > 0 and columns > 0
    - start and end are pairs (r, c) with 0 <= r < rows and 0 <= c < columns
    """
    if end == start:
        return 0

    graph = state_transitions(size) # change 1

    initial_state = (start, 1)      # change 2
    visited = {initial_state}       # change 2
    unprocessed = Queue()
    for neighbour in graph.out_neighbours(initial_state): # change 2
        unprocessed.enqueue( (neighbour, 1) )    # change 4
    while unprocessed.size() > 0:
        to_visit = unprocessed.dequeue()
        current = to_visit[0]
        length = to_visit[1]
        if current[0] == end:   # change 3
            return length
        elif current not in visited:
            visited.add(current)
            for neighbour in graph.out_neighbours(current):
                unprocessed.enqueue( (neighbour, length+1) ) # change 4
    return -1

# CELL 5

from algoesup import test

test(rook_moves, rook_moves_tests)

### 21.4.4 Complexity

#### Exercise 21.4.1