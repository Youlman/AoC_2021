from collections import defaultdict
from pprint import pprint

with open("input_day6.txt") as fin:
    input = fin.read().strip().split(",")


def lanternfish(input, number_of_days):
    frequence = defaultdict(int)
    for i in input:
        frequence[int(i)] += 1
    for _ in range(number_of_days):

        tempo_frequences = defaultdict(int)

        for key in frequence:
            if key == 0:
                tempo_frequences[6] += frequence[key]
                tempo_frequences[8] = frequence[key]
            else:
                tempo_frequences[key-1] += frequence[key]

        frequence = tempo_frequences

    return sum(frequence.values())


print(lanternfish(input, 256))
