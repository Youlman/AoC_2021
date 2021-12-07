with open('input_day2.txt', 'r') as input_day2:
    horizontal_position = 0
    depth = 0
    aim = 0
    for line in input_day2:
        direction = line.split()
        if direction[0] == 'forward':
            horizontal_position += int(direction[1])
            depth += aim*int(direction[1])
        elif direction[0] == 'down':
            aim += int(direction[1])
        elif direction[0] == 'up':
            aim -= int(direction[1])

print(horizontal_position, aim, depth, horizontal_position*depth)
