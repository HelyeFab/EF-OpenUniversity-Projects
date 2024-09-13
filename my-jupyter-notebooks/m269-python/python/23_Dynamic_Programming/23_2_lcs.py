# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 23.2 Longest common subsequence

# CELL 1

from algoesup import test

DNA_LEFT = 'A' * 6
DNA_RIGHT = 'GATTACA' * 3   # more A's than DNA_LEFT

lcs_tests = [
    # case,             left,       right,      LCS
    ('one is empty',    'hello',    '',         ''),
    ('same string',     'hello',    'hello',    'hello'),
    ('nothing common',  'yes',      'no',       ''),
    ('typical case',    'soho',     'ohio',     'oho'),
    ('subsequence',     DNA_LEFT,   DNA_RIGHT,  DNA_LEFT),
    ('substring',       'TACAG',    DNA_RIGHT,  'TACAG')
]

### 23.2.1 Recursive

#### Exercise 23.2.1

# CELL 2

# %run -i ../m269_rec_list

def lcs(left: str, right: str) -> str:
    """Return the longest common subsequence of both strings."""
    # if one or both strings are empty:
        # return the empty string
    # elif both heads are equal:
        # return the head concatenated with the LCS of both tails
    # else:
        # compute the LCS when skipping the right head
        # compute the LCS when skipping the left head
        # return the longest of the two

test(lcs, lcs_tests)
# %timeit -r 3 lcs(DNA_LEFT, DNA_RIGHT)

### 23.2.2 Top-down

#### Exercise 23.2.2

# CELL 3

# %run -i ../m269_rec_list

def lcs_topdown(left: str, right: str) -> str:
    """Return the LCS of both strings using top-down dynamic programming."""

    def lcs(left: str, right: str) -> str:
        """Auxiliary recursive function."""
        # if problem instance (left, right) isn't in cache:
            # compute LCS recursively and store it in cache
            # optional: print the cached value to see how the cache is filled
        # return the cached LCS for left and right

    cache = dict()
    return lcs(left, right)

# CELL 4

lcs_topdown('yes', 'no')

# CELL 5

test(lcs_topdown, lcs_tests)
# %timeit -r 3 lcs_topdown(DNA_LEFT, DNA_RIGHT)

### 23.2.3 Recursive with indices

#### Exercise 23.2.3

# CELL 6

def lcs_indices(left: str, right: str):
    """Return the LCS of left and right using indices, not slicing."""

    def lcs(l: int, r: int) -> str:
        """Return the LCS of left[l:] and right[r:].

        Preconditions: 0 ≤ l ≤ len(left) and 0 ≤ r ≤ len(right)
        """
        pass

    return lcs(0, 0)

test(lcs_indices, lcs_tests)
# %timeit lcs_indices(DNA_LEFT, DNA_RIGHT)

### 23.2.4 Top-down with matrix

#### Exercise 23.2.4

# CELL 7

def lcs_topdown_matrix(left: str, right: str):
    """Return the LCS of both strings using top-down dynamic programming."""

    def lcs(l: int, r: int) -> str:
        """Return the LCS of left[l:] and right[r:].

        Preconditions: 0 ≤ l ≤ len(left) and 0 ≤ r ≤ len(right)
        """
        # if lcs(l, r) isn't in cache:
            # compute it recursively and store it in cache
            # optional: print the cached value
        # return the cached lcs(l, r)

    cache = []
    for row in range(len(left) + 1):
        cache.append([None] * (len(right) + 1))
    return lcs(0, 0)

# CELL 8

lcs_topdown_matrix('soho', 'ohio')

# CELL 9

test(lcs_topdown_matrix, lcs_tests)
# %timeit lcs_topdown_matrix(DNA_LEFT, DNA_RIGHT)

### 23.2.5 Bottom-up

# CELL 10

def lcs_bottomup(left: str, right: str) -> str:
    """Return the LCS of both strings using bottom-up dynamic programming."""
    # create cache as in top-down approach
    cache = []
    for row in range(len(left) + 1):
        cache.append([None] * (len(right) + 1))

    # compute LCS bottom-up
    for l in range(len(left), -1, -1):      # last to first row
        for r in range(len(right), -1, -1): # last to first column
            if l == len(left) or r == len(right):
                cache[l][r] = ''
            elif left[l] == right[r]:
                cache[l][r] = left[l] + cache[l+1][r+1]
            else:
                skip_left = cache[l+1][r]
                skip_right = cache[l][r+1]
                if len(skip_left) > len(skip_right):
                    cache[l][r] = skip_left
                else:
                    cache[l][r] = skip_right

    # change the next line to see the contents of the matrix for other tests
    if left == 'soho' and right == 'ohio':
        for l in range(len(left) + 1):
            print(cache[l])

    # solution is in top left corner of matrix (l = r = 0)
    return cache[0][0]

test(lcs_bottomup, lcs_tests)
# %timeit lcs_bottomup(DNA_LEFT, DNA_RIGHT)

### 23.2.6 Complexity and run-time