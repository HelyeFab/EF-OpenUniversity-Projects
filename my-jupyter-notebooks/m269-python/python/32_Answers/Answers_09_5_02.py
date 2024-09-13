# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 9.5.2 answer

# CELL 1

class SMS:

    def __init__(self, filename: str):
        data = []
        with open(filename, 'r') as infile:
            for line in infile:
                pair = line.split()
                word = pair[0]
                score = int(pair[1])
                data.append( (score, word) )
        data.sort(reverse=True)
        for index in range(len(data)):
            data[index] = data[index][1]    # discard the score
        self.words = data

    def completions(self, prefix: str) -> list:
        suggestions = []
        length = len(prefix)
        for word in self.words:
            if word[:length] == prefix:
                suggestions.append(word)
                if len(suggestions) == 3:
                    return suggestions
        return suggestions