# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 22.3 Trackword

# CELL 1

vocabulary = set()
with open('enable1.txt') as file:
    for line in file:
        word = line.strip()
        if 3 <= len(word) <= 9:
            vocabulary.add(word)

### 22.3.1 The problem

### 22.3.2 Candidates and extensions

# CELL 2

def trackword(grid: list, valid: set) -> list:
    """Return all words found in the grid, in the order generated.

    Preconditions:
    - grid is a 3 by 3 table of lowercase letters
    - valid is a set of strings of allowed words
    """
    path = []           # the initial candidate
    squares = set()     # the extensions
    for row in range(3):
        for column in range(3):
            squares.add( (row, column) )
    solutions = []
    extend(path, squares, grid, valid, solutions)
    return solutions

# CELL 3

def extend(path: list, squares: set, grid: list, valid: set, solutions: list) -> None:
    """Extend the path with the squares. Add valid words to solutions."""
    if is_word(path, grid, valid):  # check the global constraints
        solutions.append(path)

# CELL 4

def path_to_string(path: list, grid: list) -> str:
    """Return the sequence of letters visited by the path in the grid."""
    string = ''
    for square in path:
        string = string + grid[square[0]][square[1]]
    return string

# CELL 5

def extend(path: list, squares: set, grid: list, valid: set, solutions: list) -> None:
    """Extend the path with the squares. Add valid words to solutions."""
    if is_word(path, grid, valid):
        solutions.append(path_to_string(path, grid))
    for square in squares:
        if can_extend(square, path, grid, valid):
            extend(path + [square], squares - {square}, grid, valid, solutions)

### 22.3.3 The constraints

# CELL 6

def is_word(path: list, grid: list, valid: set) -> bool:
    """Check if the letters in the path form a valid word."""
    return path_to_string(path, grid) in valid

# CELL 7

def can_extend(square: tuple, path: list, grid: list, valid: set) -> bool:
    """Check if square is adjacent to the last square of path."""
    if path == []:
        return True
    last_square = path[-1]
    last_row = last_square[0]
    last_column = last_square[1]
    row = square[0]
    column = square[1]
    return abs(row - last_row) < 2 and abs(column - last_column) < 2

# CELL 8

words = trackword(['set', 'err', 'vei'], vocabulary)
print('Total paths:', len(words))
print('Found 9-letter word?', 'retrieves' in words)
print('First 10:', words[:10])

# CELL 9

len(set(words))     # convert to set to remove duplicates

#### Exercise 22.3.1 (optional)

# CELL 10

# copy the functions to here

len(trackword(['set', 'err', 'vei'], vocabulary)) == 59

#### Exercise 22.3.2 (optional)

### 22.3.4 Template