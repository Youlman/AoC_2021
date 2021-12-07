with open('input_day6.txt', 'r') as input_day6:
    positions = [int(line)
                 for line in input_day6.read().strip().split(',')]


n = len(positions)
cost_fuels = {}
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(positions[j]-positions[i])
    cost_fuels[i] = sum
print(min(cost_fuels.values()))
