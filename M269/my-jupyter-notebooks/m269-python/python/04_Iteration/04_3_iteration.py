# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.3 Iteration

### 4.3.1 For-loops

# CELL 1

text = 'hello'
for character in text:
    print(character)

# CELL 2

for number in range(1, 6):  # the end number is set one higher
    print(2 * number)

# CELL 3

for number in range(-2, -1):
    print(number)

# CELL 4

for number in range(3, 3):      # no output if start = end
    print(number)

# CELL 5

for number in range(0, -1):     # no output if start > end
    print(number)

# CELL 6

for number in range(4):         # start = 0 if omitted
    print(number)

# CELL 7

text = 'hello'
for index in range(len(text)):
    print(text[index])

# CELL 8

for number in range(10, 0, -1):
    print(number)

#### Exercise 4.3.1

# CELL 9

text = 'hello'
for index in range():   # put the correct arguments in
    print(text[index])

### 4.3.2 While-loops

# CELL 10

highest = 6     # or some other value
number = 2
while number <= highest:
    print(number)
    number = number + 2

# CELL 11

highest = 6
for number in range(2, highest + 1, 2): # 2 to highest in steps of 2
    print(number)

### 4.3.3 Repeat-loops

### 4.3.4 Nested loops

# CELL 12

n = 3   # or some other positive integer
for left in range(1, n+1):
    for right in range(1, n+1):
        product = left * right
        print(left, 'x', right, '=', product)

# CELL 13

n = 3   # or some other positive integer
for left in range(1, n+1):
    for right in range(1, n+1):
        print(left, 'x', right, '=', left * right)
    print()