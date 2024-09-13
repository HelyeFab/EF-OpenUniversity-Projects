# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


#### Exercise 24.2.3 answer

# CELL 1

# %run -i ../m269_digraph

def extra_staff(project: DiGraph, people: int) -> int:
    """Return how many weeks need more than people on the project.

    Preconditions: project is acyclic, people ≥ 0
    """
    # weeks needing extra staff
    weeks = 0                           # changed

    # compute the initial in-degrees
    indegree = dict()
    for task in project.nodes():
        indegree[task] = 0
    for edge in project.edges():
        indegree[edge[1]] = indegree[edge[1]] + 1

    # compute the tasks that can be executed first
    current_week = []
    for task in project.nodes():
        if indegree[task] == 0:
            current_week.append(task)

    while len(current_week) > 0:
        if len(current_week) > people:  # changed
            weeks = weeks + 1           # changed

        next_week = []                  # added
        for task in current_week:       # added
            # simulate the removal of the executed task
            for next_task in project.neighbours(task):
                indegree[next_task] = indegree[next_task] - 1
                if indegree[next_task] == 0:
                    next_week.append(next_task)
        current_week = next_week        # added

    return weeks                        # changed