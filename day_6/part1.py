with open('input_day6.txt', 'r') as input_day6:
    state = [int(line)
             for line in input_day6.read().strip().split(',')]


def lanternfish(state, number_days):
    for _ in range(number_days):
        n = len(state)
        for j in range(n):
            if state[j] != 0:
                state[j] -= 1
            else:
                state[j] = 6
                state.append(8)

    return len(state)


print(lanternfish(state, 256))
