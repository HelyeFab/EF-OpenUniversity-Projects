# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 6.5 Dynamic arrays

### 6.5.1 The `DynamicArray` class

# CELL 1

# %run -i ../m269_array

# CELL 2

# this code is also in m269_array.py

class DynamicArray(StaticArray):
    """An array that can grow and shrink."""

    def resize(self, length: int) -> None:
        """Shorten or extend the array to the new length.

        Preconditions: 0 <= length; length != self.length()
        Postconditions: if pre-self is a_0, a_1, ..., a_n then
        post-self is b_0, b_1, ..., b_m with
        - n == pre-self.length() - 1
        - m == length - 1
        - b_i == a_i for every i from 0 to min(n, m)
        - b_i == None for every i from min(m, n) + 1 to m
        """
        new_array = [None] * length
        for index in range(0, min(length, self.length())):
            new_array[index] = self.items[index]
        self.items = new_array

### 6.5.2 Tests

# CELL 3

# %run -i ../m269_test

def test_resize(old_length: int, new_length: int) -> None:
    """Test resizing a dynamic array from old_length to new_length.

    Preconditions:
    - 0 <= old_length; 0 <= new_length
    - old_length != new_length
    """
    array = DynamicArray(old_length)
    for index in range(old_length):
        array.set_item(index, index)
    array.resize(new_length)
    check('new length', array.length(), new_length, array)
    for index in range(new_length):
        if index < min(old_length, new_length):
            value = index       # old item
        else:
            value = None        # new item
        check('get item', array.get_item(index), value, array)

# CELL 4

for old in (0, 1, 3, 6):
    for new in (0, 1, 3, 6):
        if old != new:
            print('Resize from', old, 'to', new)
            test_resize(old, new)