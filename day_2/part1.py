with open('input_day2.txt', 'r') as input_day2:
    horizontal_position = 0
    depth = 0
    for line in input_day2:
        direction = line.split()
        if direction[0] == 'forward':
            horizontal_position += int(direction[1])
        elif direction[0] == 'down':
            depth += int(direction[1])
        elif direction[0] == 'up':
            depth -= int(direction[1])
    print(horizontal_position, depth, horizontal_position*depth)
