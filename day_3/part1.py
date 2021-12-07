# def column(matrix, i):
#     return [row[i] for row in matrix]


with open('input_day3.txt', 'r') as input_day3:
    input = [line.strip() for line in input_day3]


def power_consumption(input):
    gamma_rate_string = ''
    epsilon_rate_string = ''
    for col in range(len(input[0])):
        number_0_bits = 0
        number_1_bits = 0
        for value in input:
            if bool(int(value[col])):
                number_1_bits += 1
            else:
                number_0_bits += 1

        if number_1_bits > number_0_bits:
            most_common_bit = '1'
            least_common_bit = '0'
        else:
            most_common_bit = '0'
            least_common_bit = '1'

        gamma_rate_string += most_common_bit
        epsilon_rate_string += least_common_bit

        gamma_rate = int(gamma_rate_string, base=2)
        epsilon_rate = int(epsilon_rate_string, base=2)
    return gamma_rate*epsilon_rate


print(power_consumption(input))
