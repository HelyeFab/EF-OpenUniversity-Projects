# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 24.5.3 answer

# CELL 1

SOLUTION = 0
VALUE = 1

def higher(grid: list) -> int:
    """Return the length of the longest path of ascending numbers in grid.

    Preconditions: grid is a table of non-negative integers
                   with r > 0 rows and c > 0 columns
    """
    path = []                       # initial candidate
    squares = set()                 # the extensions
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            squares.add( (row, column) )
    solution = [(0, 0)]             # path just with top-left square
    best = [solution, len(solution)]
    extend(path, squares, grid, best)
    return best[VALUE]

def extend(path: list, squares: set, grid: list, best: list) -> None:
    """Update best if path is a better solution, then extend it."""
    path_value = len(path)
    if path_value > best[VALUE]:
        best[SOLUTION] = path
        best[VALUE] = path_value
    for square in squares:
        if can_extend(square, path, grid):
            extend(path + [square], squares - {square}, grid, best)

def can_extend(square: tuple, path: list, grid: list) -> bool:
    """Check if square may extend the path towards a solution."""
    if path == []:      # the empty path can be extended in any way
        return True
    last_row = path[-1][0]
    last_column = path[-1][1]
    row = square[0]
    column = square[1]
    higher = grid[row][column] > grid[last_row][last_column]
    horizontal = (row == last_row) and abs(column - last_column) == 1
    vertical = (column == last_column) and abs(row - last_row) == 1
    return higher and (horizontal or vertical)