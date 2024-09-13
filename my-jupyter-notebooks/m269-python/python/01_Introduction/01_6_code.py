# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 1.6 Code cells

### 1.6.1 Executing code

# CELL 1

a_number = 45

# CELL 2

print(a_number)

### 1.6.2 Software check

# CELL 3

from networkx import Graph, draw, spring_layout

triangle = Graph()
triangle.add_edges_from([(1, 2), (2, 3), (3, 1)])
draw(triangle, pos=spring_layout(triangle, seed=1000))

### 1.6.3 Autocompleting

# CELL 4

print(a_number)

### 1.6.4 Changing the indentation

# CELL 5

def list_length(a_list):
        """Return the length of a list."""
length = 0
    for item in a_list:
length = length + 1
        return length

### 1.6.5 Finding and replacing text

# CELL 6

list_length(['on your marks', 'get set', 'go!'])

### 1.6.6 Commenting code out

# CELL 7

# a_number = 45
# my code: use an expression instead of a single value
a_number = 4 * 5
print(a_number)

### 1.6.7 Copying cells