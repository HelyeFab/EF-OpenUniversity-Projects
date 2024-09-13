# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.4 Linear search

### 4.4.1 Finding characters

#### Problem definition and instances

#### Algorithm

#### Complexity

#### Code and tests

# CELL 1

def first_index(text: str, character: str) -> int:
    """Return the lowest index of character in text.

    Preconditions: len(character) = 1
    Postconditions: if text includes character, then the output is
    the lowest index such that text[index] = character,
    otherwise the output is len(text)
    """
    for index in range(len(text)):
        if text[index] == character:
            return index
    return len(text)

# CELL 2

first_index('', 'a') == 0

# CELL 3

first_index('all', 'a') == 0

# CELL 4

first_index('abracadabra', 'c') == 4

# CELL 5

first_index('hi!', '!') == 2

# CELL 6

first_index('abracadabra', 'b') == 1

# CELL 7

first_index('abracadabra', 'k') == 11

#### Performance

# CELL 8

text = 100 * 'blah'   # start with a not too short string
# %timeit -r 3 -n 1000 first_index(text, '!')
text = 200 * 'blah'
# %timeit -r 3 -n 1000 first_index(text, '!')
text = 400 * 'blah'
# %timeit -r 3 -n 1000 first_index(text, '!')
text = 800 * 'blah'
# %timeit -r 3 -n 1000 first_index(text, '!')

### 4.4.2 Valid password

#### Exercise 4.4.1

#### Algorithm

#### Exercise 4.4.2

#### Exercise 4.4.3

#### Complexity

#### Exercise 4.4.4

#### Exercise 4.4.5

# CELL 9

# replace this with your code