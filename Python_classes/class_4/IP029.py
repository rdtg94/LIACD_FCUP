import math

def hypotenuse(a, b):
    hip = math.sqrt((a**2) + (b**2))
    return hip


print(round(hypotenuse(3, 4), 2))
print( round(hypotenuse(783, 42),    2) )
print( round(hypotenuse(36.5, 8.72), 2) )