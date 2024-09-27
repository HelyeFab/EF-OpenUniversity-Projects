# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 4.2 Strings

### 4.2.1 Literals

# CELL 1

"""Rick: And remember, this gun's pointed right at your heart.
Louis: That is my least vulnerable spot."""

# CELL 2

print("""Rick: And remember, this gun's pointed right at your heart.
Louis: That is my least vulnerable spot.""")

#### Mistakes

# CELL 3

‘Game over ...’

# CELL 4

'holy guacamole!"

# CELL 5

"Rick: And remember, this gun's pointed right at your heart.
Louis: That is my least vulnerable spot."

### 4.2.2 Inspecting strings

#### Length

# CELL 6

len('')     # length of the empty string

# CELL 7

len("""
Hello!
""")        # string includes 2 newline characters, but no quotes

#### Indexing

# CELL 8

'hello'[0]          # retrieve the first character

# CELL 9

'hello'[5 - 1]      # the index can be an integer expression

# CELL 10

'hello'[-1]

# CELL 11

text = 'hello'
text[len(text) - 1]     # the same as text[-1]

#### Comparisons

# CELL 12

'Tweedledee' == 'Tweedledum'

# CELL 13

'hello' < 'high'        # e comes before i, so 'hello' < 'high'

# CELL 14

'underpass' > 'under'

# CELL 15

'aardvark' < 'Zeus'     # A-Z comes before a-z in Unicode

# CELL 16

'exposé' < 'exposed'    # accented letters come after non-accented

# CELL 17

'Aardvark' < 'Zeus'     # capital first letter, rest lowercase

# CELL 18

character = '!'
'a' <= character <= 'z'     # is the character a lowercase letter?

# CELL 19

min('Zeus')         # in Unicode, A-Z comes before a-z

# CELL 20

max('By Jove!')     # in Unicode, space and ! come before A-Z

#### Membership

# CELL 21

'pose' in 'exposed'

# CELL 22

'hello' in 'Hello, world!'      # h and H are different characters

# CELL 23

',' in 'Hello, world!'  # does the string contain a comma?

# CELL 24

'hello' not in 'Hello, world!'

#### Exercise 4.2.1

# CELL 25

character = '6'
# replace this by your expression

#### Mistakes

# CELL 26

'hello'[5]  # there's no 6th character, counting from the start

# CELL 27

'hello'[-6] # there's no 6th character, counting from the end

# CELL 28

'five' < 5

#### Exercise 4.2.2

### 4.2.3 Creating strings

#### Concatenation

# CELL 29

'Hello,' + 'world!'     # concatenation doesn't add spaces

# CELL 30

'Hello' + ', ' + 'world' + '!'

# CELL 31

3 * 'Ho'    # thus spoke Father Christmas

# CELL 32

'Ho' * 0    # repeating zero times produces the empty string

#### Exercise 4.2.3

#### Slicing

# CELL 33

'hello'[0:1]        # indices 0 to 0, i.e. 'hello'[0]

# CELL 34

'hello'[1:4]        # indices 1 to 3, i.e. 2nd to 4th character

# CELL 35

'hello'[3:3]        # if start = end, the slice is empty

# CELL 36

'hello'[2:1]        # if start > end, the slice is empty

# CELL 37

'hello'[2:-1]       # 3rd to penultimate character (-1 not included)

# CELL 38

'hello'[1:4]        # len(text[start:end]) = end - start

# CELL 39

'hello'[0:1] + 'hello'[1:4]     # text[a:b] + text[b:c] = text[a:c]

# CELL 40

text = 'Alice and Bob'
middle = len(text) // 2
text[middle:len(text)] + text[0:middle]

# CELL 41

text[middle:] + text[:middle]

#### Exercise 4.2.4

#### Conversion

# CELL 42

str(2020)

#### Exercise 4.2.5

#### Mistakes

# CELL 43

3 + '3'

# CELL 44

'high' * 5.0

# CELL 45

'Ho' * -5

#### Exercise 4.2.6

# CELL 46

text = 'hello'
times = 3
# replace this by your expression