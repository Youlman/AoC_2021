
with open('input_day3.txt', 'r') as input_day3:
    input = [line.strip() for line in input_day3]


def oxygen_generator_rating(input):
    var_input = input
    for i in range(len(input[0])):
        number_0_bits = 0
        number_1_bits = 0
        position_numbers_1_bits = []
        position_numbers_0_bits = []
        if len(var_input) > 1:
            for value in var_input:
                if bool(int(value[i])):
                    number_1_bits += 1
                    position_numbers_1_bits.append(value)
                else:
                    number_0_bits += 1
                    position_numbers_0_bits.append(value)
            if number_1_bits > number_0_bits:
                var_input = position_numbers_1_bits
            elif number_1_bits < number_0_bits:
                var_input = position_numbers_0_bits
            else:
                var_input = position_numbers_1_bits
        else:
            break
    return int(var_input[0], base=2)


def co2_scrubber_rating(input):
    var_input = input
    for i in range(len(input[0])):
        number_0_bits = 0
        number_1_bits = 0
        position_numbers_1_bits = []
        position_numbers_0_bits = []
        if len(var_input) > 1:
            for value in var_input:
                if bool(int(value[i])):
                    number_1_bits += 1
                    position_numbers_1_bits.append(value)
                else:
                    number_0_bits += 1
                    position_numbers_0_bits.append(value)
            if number_0_bits < number_1_bits:
                var_input = position_numbers_0_bits
            elif number_0_bits > number_1_bits:
                var_input = position_numbers_1_bits
            else:
                var_input = position_numbers_0_bits
        else:
            break

    return int(var_input[0], base=2)


print(oxygen_generator_rating(input), co2_scrubber_rating(input),
      oxygen_generator_rating(input)*co2_scrubber_rating(input))
