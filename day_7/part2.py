from collections import defaultdict
from pprint import pprint


# print(lanternfish(input, 256))


with open('input_day6.txt', 'r') as input_day6:
    positions = [int(line) for line in input_day6.read().strip().split(',')]
    frequence = defaultdict(int)
    for i in positions:
        frequence[i] += 1


def fuel_crab(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


# solution 1

n = max(positions)
m = len(positions)
cost_fuels = {}
for i in range(n):
    fuel = 0
    for j in range(m):
        fuel += fuel_crab(abs(positions[j]-i))
    cost_fuels[i] = fuel

print(min(cost_fuels.values()))

# Solution 2

n = max(frequence)
m = len(frequence)
cost_fuels = defaultdict(int)
for i in range(n):
    fuel = 0
    for key, value in frequence.items():
        fuel += fuel_crab(abs(key-i))*value
    cost_fuels[i] = fuel

print(min(cost_fuels.values()))
