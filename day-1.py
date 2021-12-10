def sonar_sweep():
    with open('input_data.txt') as f:
        data = []
        for line in f:
            data.append(int(line.split('\n')[0]))

    increases = 0
    for i in range(1, len(data)):
        if sum(data[i:i+3])  > sum(data[i-1: i+2]):
            increases += 1
    return increases

print(sonar_sweep())