def square_number(x):
    return x ** 2


print(square_number(8))


def biggest(first: int, second: int) -> str:
    '''Return the largest of the two values.

    Postconditions:
    return first if first > second, otherwise return second
    '''
    if first > second:
        return "first"
    else:
        return "second"


print(biggest(13, 5))