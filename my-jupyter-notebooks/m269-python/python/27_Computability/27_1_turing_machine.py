# The code below was automatically extracted from
# 'Algorithms, Data Structures and Computability' by Michel Wermelinger
# Copyright (c) 2020–2024 The Open University

# You may study, execute and modify the code only if you
# are or have been enrolled in the Open University module M269.
# The code is subject to the other restrictions of the full
# copyright notice given in the book.


## 27.1 Turing machine

### 27.1.1 Definition

### 27.1.2 Parity bit

### 27.1.3 Implementation

# CELL 1

RIGHT = 1
LEFT = -1
STAY = 0

parity = {
    ('start', None):    (None, RIGHT, 'even'),

    ('even', None):     (0, LEFT, 'back'),
    ('even', 0):        (0, RIGHT, 'even'),
    ('even', 1):        (1, RIGHT, 'odd'),

    ('odd', None):      (1, LEFT, 'back'),
    ('odd', 0):         (0, RIGHT, 'odd'),
    ('odd', 1):         (1, RIGHT, 'even'),

    # ('back', None):   stop
    ('back', 0):        (0, LEFT, 'back'),
    ('back', 1):        (1, LEFT, 'back')
}

# CELL 2

wrong_parity = {
    # wrong name for initial state
    ('begin', None):    (None, RIGHT, 'even'),
    # state, symbol and movement in wrong order
    (None, 'even'):     (0, 'back', LEFT),
    # movement is missing
    ('even', 1):        (1, 'odd'),
    # typo in state name leads to unreachable state
    ('eben', 0):        (0, RIGHT, 'even')
}

# CELL 3

# this code is also in m269_tm.py

def check_TM(tm:dict) -> None:
    """Check if `tm` is well defined, printing appropriate messages."""
    if not isinstance(tm, dict):
        print('ERROR: the transition table is not a dictionary')
        return
    from_states = set()
    to_states = set()
    ok = True
    for (key, value) in tm.items():
        if not isinstance(key, tuple) or len(key) != 2:
            print('ERROR in', key, ': not a tuple (state, symbol)')
            ok = False
        elif not isinstance(key[0], str):
            print('ERROR in', key, ': state', key[0], 'is not a string')
            ok = False
        else:
            from_states.add(key[0])
        if not isinstance(value, tuple) or len(value) != 3:
            print('ERROR in', value, ': not a tuple (symbol, movement, state)')
            ok = False
        elif value[1] not in (-1, 0, 1):
             print('ERROR in', value, ': movement', value[1], 'is not -1, 0 or 1')
        elif not isinstance(value[2], str):
            print('ERROR in', value, ': state', value[2], 'is not a string')
            ok = False
        else:
            to_states.add(value[2])
    if 'start' not in from_states:
        print('ERROR: no state named "start"')
        ok = False
    unreachable = from_states - to_states - {'start'}
    if unreachable:
        print('ERROR: no transitions to states', unreachable)
        ok = False
    if ok:
        print('OK: transition table seems to be well defined')

# CELL 4

check_TM(parity)

# CELL 5

check_TM(wrong_parity)

# CELL 6

# this code is also in m269_tm.py

RIGHT = 1
LEFT = -1
STAY = 0
MAX_STEPS = 100

def run_TM(tm:dict, tape:list, debug:bool) -> list:
    """Run Turing machine `tm` on `tape` and return the resulting output.

    Run the machine from state 'start' until it has done MAX_STEPS or it halts
    (no transition for current state and symbol). In both cases, return
    the list of symbols from the final position of the head onwards.
    If the head moves to the left of the start of the tape, return the empty list.

    If debug is True, print each configuration.

    Preconditions:
    - tm maps (state, symbol) pairs to (symbol, movement, state) triples
        - states are represented by strings
        - symbols are of any hashable type
        - movement is one of RIGHT, LEFT, STAY
    - tape is a list of symbols
        - the blank symbol is represented as None
    """
    head = 0
    if tape == []:
        tape = [None]
    symbol = tape[head]
    state = 'start'
    step = 0
    if debug:
        print(step, state, tape[:head], symbol, tape[head+1:])
    while step < MAX_STEPS and (state, symbol) in tm:
        actions = tm[(state, symbol)]
        tape[head] = actions[0]     # write symbol (may be the same)
        head = head + actions[1]    # move left, right or stay
        state = actions[2]          # next state (may be the same)
        step = step + 1

        if head < 0:
            print('ERROR: head has moved left of the start position')
            return []
        elif head == len(tape):
            tape.append(None)       # extend tape when needed

        symbol = tape[head]
        if debug:
            print(step, state, tape[:head], symbol, tape[head+1:])
    if step == MAX_STEPS:
        print('WARNING: maximal steps reached; could be long input or infinite loop')
    output = tape[head:]
    while output != [] and output[-1] == None:
        output.pop(-1)
    return output

# CELL 7

run_TM(parity, [None, 1, 0, 1], True)

# CELL 8

from algoesup import test

parity_tests = [
    # name,         machine,    input,  debug,  output
    ('no bits',     parity,    [None],  False,  [None, 0]),
    ('just 0',      parity, [None, 0],  False,  [None, 0, 0]),
    ('just 1',      parity, [None, 1],  False,  [None, 1, 1]),
]

test(run_TM, parity_tests)

### 27.1.4 Checking passwords

#### Exercise 27.1.1

#### Exercise 27.1.2

# CELL 9

from algoesup import test

is_valid = {
    ('start', 'a'):     ('a', RIGHT, 'letter'),
    ('start', '0'):     ('0', RIGHT, 'digit'),
}

check_TM(is_valid)

is_valid_tests = [
    # case,         TM,        input,            debug,  output
    ('empty pwd',   is_valid,  [None],           False,  [False]),
    ('no digits',   is_valid,  ['a', 'a'],       False,  [False]),
    ('no letters',  is_valid,  ['0'],            False,  [False]),
    ('both',        is_valid,  ['0', 'a', '0'],  False,  [True])
]

test(run_TM, is_valid_tests)

#### Exercise 27.1.3

#### Exercise 27.1.4