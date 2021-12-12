init = [3,4,3,1,2]

# Part 1 solution. Too slow for part 2 :(
def spawn(fish, count=0, prev_born=0):
    new_fish =[*fish]
    born_next = 0
    for idx, num in enumerate(new_fish):
        if num == 1:
            born_next += 1
        if num == 0:
            new_fish[idx] = 6
        else:
            new_fish[idx] -= 1
    
    if prev_born > 0:
        for i in range(0,prev_born):
            new_fish.append(8)
    if count == 80: 
        return len(fish)
    
    return spawn(new_fish, count + 1, born_next)

print(spawn(init))

# PART 2 Solution

def solution(input):
    fish = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        0: 0,  
    }

    for num in input:
        fish[num] += 1
    
    print(fish)

    count = 0
    while count < 256:

        new_state = {}

        if 1 in fish and fish[1] > 0:
            new_state[0] = fish[1]
        if 2 in fish and fish[2] > 0:
            new_state[1] = fish[2]
        if 3 in fish and fish[3] > 0:
            new_state[2] = fish[3]
        if 4 in fish and fish[4] > 0:
            new_state[3] = fish[4]
        if 5 in fish and fish[5] > 0:
            new_state[4] = fish[5]
        if 6 in fish and fish[6] > 0:
            new_state[5] = fish[6]
        if 7 in fish and fish[7] > 0:
            new_state[6] = fish[7]
        if 8 in fish and fish[8] > 0:
            new_state[7] = fish[8]
        if 0 in fish and fish[0] > 0:
            if 8 in new_state:
                new_state[8] += fish[0]
            elif 8 not in new_state:
                new_state[8] = fish[0]
            if 6 in new_state:
                new_state[6] += fish[0]
            elif 6 not in new_state:
                new_state[6] = fish[0]
        fish = new_state
        count +=1

    import functools
    return functools.reduce(lambda a, b: a+b, fish.values())


print(solution(init))
