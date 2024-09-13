# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 8.4.4 answer

# CELL 1

def certificates(ranking: list) -> list:
    best_teams = []
    awarded_schools = set()
    for team in ranking:
        school = team[:-1]   # school name without digit
        if school not in awarded_schools:
            awarded_schools.add(school)
            best_teams.append(team)
    return best_teams

certificates_tests = [
    # case,         ranking,                    certificates
    ('3 schools',   ['C1','B2','B1','A1','C2'], ['C1','B2','A1']),
    # new tests:
    ('1 team',      ['A1'],                     ['A1']),
    ('1 school',    ['C3', 'C1', 'C2'],         ['C3']),
    ('1 team per school', ['C1', 'B1', 'A1'],   ['C1', 'B1', 'A1'])
]