# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 24.2 Extra staff

### 24.2.1 Exercises

#### Exercise 24.2.1

#### Exercise 24.2.2

#### Exercise 24.2.3

# CELL 1

# %run -i ../m269_digraph
from algoesup import test

def extra_staff(project: DiGraph, people: int) -> int:
    """Return how many weeks need more than people on the project.

    Preconditions: project is acyclic, people ≥ 0
    """
    pass

project = DiGraph()
for task in range(9):
    project.add_node(task)
project.add_edge(1, 0)
project.add_edge(1, 6)
project.add_edge(0, 5)
project.add_edge(0, 6)
project.add_edge(5, 8)
project.add_edge(8, 6)
project.add_edge(8, 7)
project.add_edge(4, 2)
project.add_edge(4, 3)

extra_staff_tests = [
    # case,      project, people, weeks
    ("0 people", project, 0,      5),
    ("1 person", project, 1,      3),
    ("2 people", project, 2,      1),
    ("3 people", project, 3,      0),
]

test(extra_staff, extra_staff_tests)