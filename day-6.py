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
