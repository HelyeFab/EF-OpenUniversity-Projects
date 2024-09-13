# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 8.2.3 answer

# CELL 1

from algoesup import test

def invert(original: dict) -> dict:
    inverted = dict()
    for (word, translations) in original.items():
        for translation in translations:
            if translation not in inverted:
                inverted[translation] = [word]
            else:
                inverted[translation].append(word)
    return inverted