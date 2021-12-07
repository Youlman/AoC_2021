with open("input_day1.txt", "r") as input_day1:
    input = [int(line.strip()) for line in input_day1]


def count_difference_greater(input):
    count = 0
    for i in range(len(input)-1):
        if input[i+1] > input[i]:
            count += 1
    return count


three_measurements_windows = []
for i in range(len(input)-2):
    three_sum = input[i] + input[i+1] + input[i+2]
    three_measurements_windows.append(three_sum)

print(count_difference_greater(three_measurements_windows))
