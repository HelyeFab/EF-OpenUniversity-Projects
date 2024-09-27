# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 8.2 Dictionaries

# CELL 1

pt_to_en = dict()   # Portuguese to English dictionary
pt_to_en['alface'] = ['lattice']
pt_to_en['alface'] = ['lettuce']    # replace wrong entry
pt_to_en['carro'] = ['car']
pt_to_en['andar'] = ['floor', 'walk']
'carro' in pt_to_en

# CELL 2

for word in pt_to_en:   # iterate over the keys
    for translation in pt_to_en[word]:
        print(word, 'means', translation)

# CELL 3

for pair in pt_to_en.items():
    word = pair[0]
    for translation in pair[1]:
        print(word, 'means', translation)

# CELL 4

for (word, translations) in pt_to_en.items():
    for translation in translations:
        print(word, 'means', translation)

# CELL 5

pt_to_en = {
    'alface': ['lettuce'],
    'carro': ['car'],
    'andar': ['floor', 'walk']
}

# CELL 6

our_houses = {23: 'Alice', 45: 'Bob'}

# CELL 7

our_street = {45: 'Bob', 23: 'Alice'}
our_street == our_houses

# CELL 8

our_street != {45: 'Bob', 23: 'Alissa'}

# CELL 9

pt2en = {
    'alface': {'noun': 'lettuce'},
    'carro': {'noun': 'car'},
    'andar': {'noun': 'floor', 'verb': 'walk'}
}

# CELL 10

inner_dictionary = pt2en['andar']
print(inner_dictionary['verb'])
print(pt2en['andar']['verb'])   # shorter alternative

### 8.2.1 Mistakes

# CELL 11

pt_to_en['car']     # 'car' is among the values, not the keys

# CELL 12

'carro' in pt_to_en

# CELL 13

'car' in pt_to_en

# CELL 14

roman_to_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
for (key, value) in roman_to_arabic.items():
    roman_to_arabic[key+'I'] = value+1

# CELL 15

stock = {'trousers': 5, 't-shirt': 20, 'dress': 12}
for (key, value) in stock.items():
    stock[key] = 0      # all sold out
stock

# CELL 16

employee_by_location = {    # occupants of each building's offices
    ['Main building', 4]: ['Alice', 'Chan'],
    ['Annex', 3]: ['Bob']
}

# CELL 17

employee_by_location = {
    ('Main building', 4): ['Alice', 'Chan'],
    ('Annex', 3): ['Bob']
}

#### Exercise 8.2.1

# CELL 18

bilingual = dict()
bilingual['alface'] = 'lettuce'
bilingual['carro'] = 'car'
bilingual['andar'] = 'floor'
bilingual['andar'] = 'walk'

### 8.2.2 Using dictionaries

#### Exercise 8.2.2

#### Exercise 8.2.3

# CELL 19

from algoesup import test

def invert(original: dict) -> dict:
    """Return the inverted dictionary.

    In both dictionaries, the keys are strings and
    the values are lists of strings.

    Postconditions:
    word1 in output[word2] if and only if word2 in original[word1]
    """
    inverted = dict()
    pass
    return inverted

pt_to_en = {
    'carro': ['car'],
    'andar': ['floor', 'walk'],     # as in 'second floor'
    'chão': ['floor'],              # as in 'wooden floor'
    'saudade': []                   # translation omitted
}

en_to_pt = {
    'car' : ['carro'],
    'walk': ['andar'],
    'floor': ['andar', 'chão']
}

invert_tests = [
    #case,              a_to_b,             inverted
    ('no words',        dict(),             dict()),
    ('pt_to_en',        pt_to_en,           en_to_pt)
]

test(invert, invert_tests)