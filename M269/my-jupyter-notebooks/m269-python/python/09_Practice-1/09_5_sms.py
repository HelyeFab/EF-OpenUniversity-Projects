# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 9.5 SMS

### 9.5.1 First approach

#### Exercise 9.5.1

#### Exercise 9.5.2

# CELL 1

from algoesup import test

class SMS:
    """A collection of words for completing prefixes."""

    def __init__(self, filename: str):
        """Load the words and their scores from the given file.

        Preconditions: filename is the name of a text file where
        - each line is of the form 'word score'
        - scores are positive integers
        - words aren't empty nor repeated
        """
        pass            # create the data structure
        with open(filename, 'r') as infile:
            for line in infile:
                pair = line.split()
                word = pair[0]
                score = int(pair[1])
                pass    # process the word and score
        pass            # do any further processing

    def completions(self, prefix: str) -> list:
        """Return the highest-scoring words starting with prefix.

        Postconditions: the output is a list of at most 3 words
        from the file, ordered by descending scores
        """
        pass

words_tests_100 = [
    # case,             prefix, completions
    ('no prefix',       '',     ['the', 'of', 'and']),
    ('matches > 3',     'a',    ['and', 'as', 'at']),
    ('matches = 3',     'an',   ['and', 'an', 'any']),
    ('matches < 3',     'wi',   ['with', 'will']),
    ('matches = 0',     'z',    []),
    ('prefix = word',   'said', ['said']),
    ('last words',      'y',    ['you', 'your']),
]

sms100 = SMS('100words.txt')
test(sms100.completions, words_tests_100)

# CELL 2

words_tests_10000 = [
    # case,           prefix, completions
    ('no prefix',     '',     ['the', 'of', 'and']),
    ('matches > 3',   'a',    ['and', 'as', 'at']),
    ('matches = 3',   'anx',  ['anxious', 'anxiety', 'anxiously']),
    ('matches < 3',   'tric', ['trick', 'tricks']),
    ('matches = 0',   'glu',  []),
    ('prefix = word', 'said', ['said']),
    ('last words',    'zo',   ['zone']),
]

sms10000 = SMS('10000words.txt')
test(sms10000.completions, words_tests_10000)

#### Exercise 9.5.3

# CELL 3

print('100 words:')
for test in words_tests_100:
    prefix = test[1]
    print("'" + prefix + "'")
    # %timeit -r 5 -n 10000 sms100.completions(prefix)
print('\n10,000 words:')
for test in words_tests_10000:
    prefix = test[1]
    print("'" + prefix + "'")
    # %timeit  -r 5 -n 1000 sms10000.completions(prefix)

### 9.5.2 Second approach

#### Exercise 9.5.4

#### Exercise 9.5.5 (optional)