
from typing import Callable

def test(function: Callable, test_table: list) -> None:
    """Test the function with the test_table. Report failed tests.

    Preconditions: each element of test_table is a list or tuple with
        - a string (the test case name)
        - one or more values (the inputs to the function)
        - the expected output value
    """
    for test_case in test_table:
        name = test_case[0]
        inputs = test_case[1:-1]
        expected = test_case[-1]
        actual = function(*inputs)
        if actual != expected:
            print(name, 'FAILED:', actual, 'instead of', expected)
    print('Tests finished.')

def check(case: str, actual: object, expected: object, context: object) -> None:
    """Write a message if actual and expected are different."""
    if actual != expected:
        print(case, 'FAILED for', context, ':', actual, 'instead of', expected)
