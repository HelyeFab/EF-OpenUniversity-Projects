# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.5 Tuples and tables

### 4.5.1 Literals and operations

# CELL 1

len( (1, (2, 3), True) )

# CELL 2

(1, (2, 3), True)[1]    # indexing: 2nd item is a pair of integers

# CELL 3

(1, 2, 3) < (1, 4, 3)   # comparison: item by item

# CELL 4

(1, (2, 3), True)[1:3]  # slicing: 2nd to 3rd items

# CELL 5

min((3, 4, -2, 7, 9))   # extra parentheses for the tuple

# CELL 6

2 in (1, 2, 3)          # (1, 2, 3) does have member 2

# CELL 7

(1, 2) in (1, 2, 3)     # (1, 2, 3) doesn't have member (1, 2)

# CELL 8

(1, 2) in ((1, 2), 3)   # ((1, 2), 3) does have member (1, 2)

# CELL 9

tuple('hello')

# CELL 10

tuple(range(1, 4))

# CELL 11

for item in (1, (2, 3), True):
    print(item)

### 4.5.2 Mistakes

# CELL 12

(1 (2, 3), True)

# CELL 13

(3) + (4)       # arithmetic expression with redundant parentheses

# CELL 14

(3,) + (4,)     # concatenation of tuples of length 1

# CELL 15

tuple(True)

### 4.5.3 Tables

# CELL 16

games_by_row = (                        # each item is a row
    ('Board game', 'Rating', 'Owned'),  # header row
    ('Power Grid',      10 ,   True ),  # first data row
    (   'Vintage',       8 ,   True ),
    (  'Pandemic',       9 ,  False )
)

# CELL 17

games_by_row

# CELL 18

row_index = 1                   # Power Grid is in the 2nd row
column_index = 2                # ownership is in the 3rd column
row = games_by_row[row_index]
cell = row[column_index]
cell

# CELL 19

games_by_row[1][2]  # 2nd row, 3rd column

# CELL 20

games_by_row[2][1]  # 3rd row (Vintage), 2nd column (Rating)

# CELL 21

GAME = 0
RATING = 1
OWNED = 2

# CELL 22

games_by_row[1][OWNED]

# CELL 23

games_by_row[2][RATING]

#### Exercise 4.5.1

# CELL 24

games_by_column = (                     # each item is a column
    ('Board game', 'Power Grid', 'Vintage', 'Pandemic'),
    ('Rating',              10 ,        8 ,         9 ),
    ('Owned',             True ,     True ,     False )
)

# CELL 25

# replace with your expression

### 4.5.4 Iterating

# CELL 26

total = 0
count = 0
for row in range(1, len(games_by_row)):    # skip header row
    count = count + 1
    total = total + games_by_row[row][RATING]
print(total / count)

# CELL 27

total = 0
for row in range(1, len(games_by_row)):    # skip header row
    total = total + games_by_row[row][RATING]
print(total / (len(games_by_row) - 1))

# CELL 28

for row in games_by_row:
    for cell in row:
        print(cell)

# CELL 29

for column in range(len(games_by_row[0])):
    for row in range(len(games_by_row)):
        print(games_by_row[row][column])

#### Exercise 4.5.2

# CELL 30

tic_tac_toe = (
    ('X', 'O', 'X'),
    (' ', 'X', ' '),
    ('O', ' ', 'O')
)

# CELL 31

# replace with your code

#### Exercise 4.5.3