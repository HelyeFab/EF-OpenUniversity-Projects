
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
