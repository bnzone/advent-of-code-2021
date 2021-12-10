def dive():
    with open('input_data.txt') as f:
        formatted = [row.split() for row in f]
    forward = 0
    depth = 0
    aim = 0
    for move in formatted:
        if move[0] == 'forward':
            forward += int(move[1])
            depth += aim * int(move[1])
        elif move[0] == 'up':
            aim -= int(move[1])
        else:
            aim += int(move[1])
    return forward * depth
    
print(dive())