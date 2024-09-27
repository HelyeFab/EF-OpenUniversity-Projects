# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 8.3 Hash tables

### 8.3.1 With separate chaining

# CELL 1

[   # lookup table
    [('Carol', 599)],               # first slot
    [('Bob', 407), ('Alice', 312)], # second slot
    []                              # third slot
]

#### Exercise 8.3.1

### 8.3.2 Hash functions

# CELL 2

def hash_string(string: str) -> int:
    product = 1
    for character in string:
        product = product * ord(character)
    return product

# CELL 3

hash_string('algorithm')

# CELL 4

hash_string('algorythm')

# CELL 5

hash_string('logarithm')    # same as for 'algorithm'

# CELL 6

hash('algorithm')

# CELL 7

hash('logarithm')

### 8.3.3 Unhashable values

# CELL 8

hash((1, 2, 3))

# CELL 9

hash([1, 2, 3])

### 8.3.4 Complexity

### 8.3.5 Implementation

# CELL 10

class HashMap:
    """An unordered collection of key-value pairs.

    Keys must be unique and hashable.
    """

    # The hash table is a dynamic array of slots.
    # Each slot is a dynamic array of key-value pairs.

    def __init__(self):
        self.slots = [ [] ]     # start with 1 slot
        self.size = 0

    def has(self, key: object) -> bool:
        """Return True if and only if key is in the map.

        Preconditions: key is hashable
        """
        index = hash(key) % len(self.slots)
        slot = self.slots[index]
        # linear search of the key in the only slot it can be
        for pair in slot:
            if pair[0] == key:
                return True
        return False

    def grow(self) -> None:
        """Grow the dictionary if necessary.

        Postconditions:
        if pre-self has load factor 1, post-self has load factor 0.5
        """
        capacity = len(self.slots)
        if self.size == capacity:
            # new hash table with double the slots, all empty
            new_capacity = capacity * 2
            new_slots = []
            for each_slot in range(new_capacity):
                new_slots.append([])
            # put each pair in the correct slot in the new table
            for slot in self.slots:
                for pair in slot:
                    index = hash(pair[0]) % new_capacity
                    new_slots[index].append(pair)
            # use the new hash table
            self.slots = new_slots

    def associate(self, key: object, value: object) -> None:
        """Associate value to key in the map.

        Preconditions: key is hashable
        Postconditions: looking up key in self returns value
        """
        self.grow()
        index = hash(key) % len(self.slots)
        slot = self.slots[index]
        for pair in slot:
            if pair[0] == key:
                pair[1] = value
                return
        slot.append( [key, value] )
        self.size = self.size + 1

# CELL 11

characters = HashMap()
for letter in 'algorithm':
    characters.associate(ord(letter), letter)
    print(characters.slots)
for letter in 'moralgith':      # test membership operation
    if not characters.has(ord(letter)):
        print('error: missing', letter)

#### Exercise 8.3.2

#### Exercise 8.3.3