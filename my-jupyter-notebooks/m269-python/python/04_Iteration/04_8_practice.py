# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.8 Optional practice

### 4.8.1 DNA

#### Exercise 4.8.1

### 4.8.2 Minimum

#### Exercise 4.8.2

### 4.8.3 Lexicographic comparison

#### Exercise 4.8.3

### 4.8.4 Palindrome

#### Exercise 4.8.4

### 4.8.5 Mode

#### Exercise 4.8.5

### 4.8.6 Images

# CELL 1

# %run -i ../m269_image

cover = load_image('../cover.jpg')
print('Image has', width(cover), 'x', height(cover), 'pixels.')
show_image(cover)

# CELL 2

def swap_RB(image: list) -> None:
    """Swap red and blue components of each pixel."""
    for column in range(width(image)):
        for row in range(height(image)):
            pixel = image[row][column]
            image[row][column] = (pixel[B], pixel[G], pixel[R])

swap_RB(cover)
show_image(cover)

# CELL 3

def stripes(n: int, colour1: tuple, colour2: tuple) -> list:
    """Create n pairs of alternating stripes, each 100 x 5 pixels.

    Preconditions: n > 0; colour1 and colour2 are RGB triplets
    Postconditions: the top stripe has colour1
    """
    image = new_image(100, n * 2 * 5, colour2)
    # add 5 rows of colour1 every 10 rows
    for row in range(0, height(image), 10):
        for increment in range(0, 5):
            image[row + increment] = [colour1] * 100
    return image

image = stripes(5, NAVY, SILVER)
show_image(image)

#### Exercise 4.8.6

# CELL 4

# replace this with your code