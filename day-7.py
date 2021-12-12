# (Part 1 is simple math, just find the median of the input and then subtract the values
# from the median to get the fuel)

# Part 2 solution 


average_0 = sum(input) / len(input)
average = int(round(average_0) - 1)

def solution(input):
    total_fuel = 0
    for crab_num in input:
        position = abs(crab_num - average)
        crab_fuel = fuel_counter(position)
        total_fuel += crab_fuel
    return total_fuel
        

def fuel_counter(position):
    crab_fuel = 0
    for i in range(1, position + 1):
        crab_fuel += i
    return crab_fuel

print(solution(input))
