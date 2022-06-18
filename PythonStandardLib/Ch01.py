# Python round, absolute value, exponents
import math
from re import M


# round
# first decimal 4 or below, round down
# first decimal 5 or above, round up

print(round(3.6))

# sorted()
leaderBoard = {431: "ABC", 123: "MCL", 312:"TYU"}
print(sorted(leaderBoard, reverse=True))

# Constants
print(math.pi)
math.e
math.nan
math.inf
-math.inf

# Trigonometry
obst_direction = math.cos(math.pi / 4)
print(obst_direction)

# Ceiling and floor
math.ceil(10.3) # -> 11

# Factorial and square root
print(math.factorial(3))
print(math.sqrt(64))

# Greatest common denominator GCD
print(math.gcd(52, 8))

# Degrees and radians
math.radians(360)
