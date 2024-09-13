# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.6 Lists

### 4.6.1 Modifying sequences

#### Exercise 4.6.1

### 4.6.2 Creating lists

# CELL 1

to_do = [
    'finish writing this chapter',
    'write the next one',
    'rinse and repeat for another 20+ chapters'
]
to_do

# CELL 2

print(to_do)

# CELL 3

10 * [0]     # create an integer list initialised to zeroes

# CELL 4

list(range(1, 10))

# CELL 5

list('Hello, world!')

# CELL 6

board = (('X', 'O', 'X'), (' ', ' ', ' '), ('O', 'X', ' '))
list(board)     # doesn't convert nested tuples

# CELL 7

sorted('Hello, world!')

# CELL 8

sorted([2, 4, -3, 4.1])

# CELL 9

sorted([2, 4, -3, 4.1], reverse=True)   # sort in descending order

### 4.6.3 Mistakes

# CELL 10

sorted([1, 2, 3], True)     # sort in descending order

# CELL 11

[1 [2, 3], True]        # comma missing after 1

# CELL 12

['first task', 'second task'] + 'third task'

# CELL 13

(1, 2) + [3, 4]

### 4.6.4 Modifying lists

# CELL 14

daily_temperature = [-5, -2, 0, 1, -1]
daily_temperature[1] = -4

# CELL 15

daily_temperature

# CELL 16

daily_temperature.insert(0, -6)     # insert -6 at index 0
daily_temperature

# CELL 17

daily_temperature.insert(-1, 'week 2:')
daily_temperature

# CELL 18

daily_temperature = [-5, -2, 0, 1, -1]

# CELL 19

daily_temperature.insert(len(daily_temperature), 'week 2:')
daily_temperature

# CELL 20

daily_temperature.append(6)
daily_temperature

# CELL 21

daily_temperature.pop(0)  # remove first item

# CELL 22

daily_temperature.pop(-1) # remove last item

# CELL 23

daily_temperature

# CELL 24

help(list.insert)

# CELL 25

numbers = [1, 4, -2, 3]
numbers.sort()
numbers

# CELL 26

numbers.sort(reverse=True)
numbers

#### Exercise 4.6.2

# CELL 27

daily_temperature = daily_temperature + [6]

#### Exercise 4.6.3

# CELL 28

games_by_row = [
    ['Board game', 'Rating', 'Owned'],
    ['Power Grid',      10 ,   True ],
    [   'Vintage',       8 ,   True ],
    [  'Pandemic',       9 ,  False ]
]

# CELL 29

# replace this by your code to change the table
games_by_row    # display the new table

### 4.6.5 Mistakes

# CELL 30

text = 'i love grilled fish'
text[0] = 'I'

# CELL 31

pop([1, 2, 3], 1)       # there's no pop function ...

# CELL 32

[1, 2, 3].pop(1)       # but lists do have a method named pop