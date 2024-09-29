# import matplotlib.pyplot as plt
import math # for pi



print(max(3, -0.5, math.pi));
print(min(3, -0.5, math.pi));

x= 2
y= 3


def mod(x, y):
    return x-math.floor(x/y)*y

print(mod(5, -2))

def isEven(n):
    return n % 2 == 0

print(isEven(5))
print(isEven(2348))

print(6/2)
