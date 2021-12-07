with open("input_day1.txt", "r") as input_day1:
    input = [int(line.strip()) for line in input_day1]


def count_difference_greater(input):
    count = 0
    for i in range(len(input)-1):
        if input[i+1] > input[i]:
            count += 1
    return count


print(count_difference_greater(input))
