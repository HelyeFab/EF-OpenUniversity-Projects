# Exercise 2.6.1

def brick_volume(length: int, width: int, height: int) -> int:
    """Return ...
    Input: length an integer, width an integer, height an integer
    Preconditions: length > 0; width > 0; height > 0
    length, width, height are in millimeters
    Postconditions: the output is length * width * height
    Output: an integer
    """
    return length * width * height

print(brick_volume(2,3,4))  # expect 24

print(2**63) 


# Exercise 2.7.1
'''
The algorithm consists of two simple arithmetic operations:

Multiplying the radius by 2 to get the diameter.
Multiplying the diameter by π to get the length.
Each of these steps is a constant-time operation (i.e., they don't depend on the size of the input; they just involve basic arithmetic).

Thus, the time complexity of this algorithm is Θ(1), meaning it runs in constant time.
'''