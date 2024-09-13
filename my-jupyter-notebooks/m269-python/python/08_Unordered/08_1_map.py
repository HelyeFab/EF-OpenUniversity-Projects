# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 8.1 Maps

### 8.1.1 The map ADT

### 8.1.2 Using maps

#### Exercise 8.1.1

#### Exercise 8.1.2

#### Exercise 8.1.3

### 8.1.3 Lookup tables

# CELL 1

FAHRENHEIT = [0] * 101
for celsius in range(-50, 51):
    FAHRENHEIT[celsius] = celsius * 9 // 5 + 32
FAHRENHEIT = tuple(FAHRENHEIT)  # don't change table anymore

# CELL 2

cipher = 'lejqawntgckmfyrboxvhzsdipu'

# CELL 3

def index_of(character: str) -> int:
    """Return a valid index for the character.

    Preconditions: character is a lowercase English letter
    Postconditions: the output is 0 for a, 1 for b, ..., 25 for z
    """
    return ord(character) - ord('a')

# CELL 4

def encrypt(text: str, cipher: str) -> str:
    """Return the encrypted version of text, using cipher.

    Preconditions: len(cipher) = 26
    Postconditions: the output is text, with every lowercase letter
    replaced by the corresponding character in cipher
    """
    encrypted = ''
    for character in text:
        if 'a' <= character <= 'z':
            # apply hash function and lookup table
            encrypted = encrypted + cipher[index_of(character)]
        else:
            encrypted = encrypted + character
    return encrypted

encrypt('This is top secret!', cipher)

#### Exercise 8.1.4