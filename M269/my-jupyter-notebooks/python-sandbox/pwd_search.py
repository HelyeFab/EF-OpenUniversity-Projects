def is_valid_password(password):
    has_letter = False
    has_digit = False

    for character in password:
        if '0' <= character <= '9':
            has_digit = True
        if 'a' <= character <= 'z':
            has_letter = True

    is_valid = has_digit and has_letter
    return is_valid



print(is_valid_password('b3ansy-boy1'))


import timeit

# Long password example (for example, a 1000-character string with mixed letters and digits)
print(timeit.timeit('is_valid_password("a" * 500 + "1" * 500)', globals=globals(), number=1000))
# Long password example (for example, a 1000-character string with mixed letters and digits)
print(timeit.timeit('is_valid_password("a" * 500 + "1" * 500)', globals=globals(), number=1000))


def optimised_is_valid_password(password):
    has_letter = False
    has_digit = False

    for character in password:
        if '0' <= character <= '9':
            has_digit = True
        elif 'a' <= character <= 'z':
            has_letter = True
        
        # If both conditions are met, we can stop early
        if has_letter and has_digit:
            return True

    # Return False if we finish the loop without finding both
    return False


# Long password example (for example, a 1000-character string with mixed letters and digits)
print(timeit.timeit('optimised_is_valid_password("a" * 500 + "1" * 500)', globals=globals(), number=1000))
# Long password example (for example, a 1000-character string with mixed letters and digits)
print(timeit.timeit('optimised_is_valid_password("a" * 500 + "1" * 500)', globals=globals(), number=1000))



games_by_column = (                     # each item is a column
    ('Board game', 'Power Grid', 'Vintage', 'Pandemic'),
    ('Rating',              10 ,        8 ,         9 ),
    ('Owned',             True ,     True ,     False )
)

print(games_by_column[1][3])  # 