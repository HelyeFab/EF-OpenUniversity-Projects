import timeit

var1 = 2 ** 64 + 1
var2 = 2 ** 64 + 2

# Set the number of times you want to execute the expression per loop
num_executions_per_loop = 1000000

# Set the number of loops (repetitions of the timing)
num_loops = 5

# Timing the expression 'var1 + var2' using lambda and repeat
execution_times = timeit.repeat(lambda: var1 + var2, number=num_executions_per_loop, repeat=num_loops)

# Convert the time for each loop to milliseconds, microseconds, and nanoseconds
for i, execution_time in enumerate(execution_times):
    execution_time_milliseconds = execution_time * 1000
    execution_time_microseconds = execution_time * 1_000_000
    execution_time_nanoseconds = execution_time * 1_000_000_000

    print(f"Loop {i + 1}:")
    print(f"{execution_time:.10f} seconds")
    print(f"{execution_time_milliseconds:.10f} milliseconds")
    print(f"{execution_time_microseconds:.10f} microseconds")
    print(f"{execution_time_nanoseconds:.10f} nanoseconds\n")


def brick_volume(length: int, width: int, height: int) -> int:
    """Return the volume of a brick.
    Input: length an integer, width an integer, height an integer
    Preconditions: length > 0; width > 0; height > 0
    length, width, height are in millimeters
    Postconditions: the output is length * width * height
    Output: an integer
    """
    return length * width * height

l = 2
w = 3
h = 4

# Timing the function 'brick_volume' using lambda and repeat
execution_times = timeit.repeat(lambda: brick_volume(l, w, h), number=num_executions_per_loop, repeat=num_loops)
# Convert the time for each loop to milliseconds, microseconds, and nanoseconds
for i, execution_time in enumerate(execution_times):
    execution_time_milliseconds = execution_time * 1000
    execution_time_microseconds = execution_time * 1_000_000
    execution_time_nanoseconds = execution_time * 1_000_000_000

    print(f"Loop  {i + 1} - Brick Volume function:")
    print(f"{execution_time:.10f} seconds")
    print(f"{execution_time_milliseconds:.10f} milliseconds")
    print(f"{execution_time_microseconds:.10f} microseconds")
    print(f"{execution_time_nanoseconds:.10f} nanoseconds\n")