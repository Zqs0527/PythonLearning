import random
import statistics
import itertools
print(random.random())

print(random.randrange(2,19))

# Generate a collection of random numbers
lottery_winners = random.sample(range(100), 5)
print(lottery_winners)

agesData = random.sample(range(10, 78), 6)
print(agesData)
print(type(agesData))

print(statistics.mean(agesData))
print(statistics.median(agesData))
print(statistics.mode(agesData))
