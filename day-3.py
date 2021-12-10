# ~~~~~~~~~~~  Part 1  ~~~~~~~~~~~~~~~~

def binary_diagnostic():
    with open('input_data.txt') as f:
        test = [row.strip() for row in f]
    
    binary_len = len(test[0])
    last_index = binary_len - 1
    i = 0
    gamma = []
    epsilon = []

    while i <= last_index:
        ones = 0
        zeros = 0
        for row in test:
            if row[i] == '0':
                zeros += 1
            else:
                ones += 1
        if ones > zeros:
            gamma.append('1')
        else:
            gamma.append('0')
        i += 1

    for binary_values in gamma:
        if binary_values == '1':
            epsilon.append('0')
        else:
            epsilon.append('1')
            
    num_gamma = int(''.join(gamma), 2)
    num_epsilon = int(''.join(epsilon), 2)
    return num_gamma * num_epsilon


print(binary_diagnostic())


# ~~~~~~~~~~~  Part 2  ~~~~~~~~~~~~~~~~


def filter_stuff(winner, idx, lst):
    """
    - Takes in a list, an index and a winner ('1' or '0'). 
    - Filters the list so it only has the winners
    """
    return list(filter(lambda row: row[idx] == winner, lst))

def ones_zeros_winner_oxygen(lst, INDEX):
    """
     - Takes in a list and an index where to look (column)
     - Finds the winner in the specified index ('1' or '0')
     - After it finds the winner -> call a filter functions at
        gives it the list to filter, who is the winner, and at what index
        to filter
    """
    max_idx = len(lst[0]) - 1
    if INDEX > max_idx: 
        return []
    ones = 0
    zeros = 0

    for row in lst:
        if row[INDEX] == '1':
            ones += 1
        else:
            zeros += 1
    # Finding the winner by comparing number of 1s and 0s     
    winner = None
    if ones < zeros:
        winner = '0'
    else:
        winner = '1'
    result = filter_stuff(winner, INDEX, lst)
    return result

def ones_zeros_winner_co2(lst, INDEX):
    """
     - Takes in a list and an index where to look (column)
     - Finds the winner in the specified index ('1' or '0')
     - After it finds the winner -> call a filter functions at
        gives it the list to filter, who is the winner, and at what index
        to filter
    """
    max_idx = len(lst[0]) - 1
    if INDEX > max_idx: 
        return []
    ones = 0
    zeros = 0

    for row in lst:
        if row[INDEX] == '1':
            ones += 1
        else:
            zeros += 1
    # Finsing the winner by comparing number of 1s and 0s     
    winner = None
    if ones < zeros:
        winner = '1'
    else:
        winner = '0'
    result = filter_stuff(winner, INDEX, lst)
    return result


def oxygen_rating(lst, index = 0): # ['10010'].  
    if len(lst) < 2:
        return lst
    # get fully filtered list at a specified index                
    filtered = ones_zeros_winner_oxygen(lst, index) 

    # repeat the same thing but with new list and next index (+1)
    return oxygen_rating(filtered, index + 1)

def co2_rating(lst, index=0):
    if len(lst) < 2:
        return lst
    filtered = ones_zeros_winner_co2(lst, index)

    # repeat the same thing but with new list and next index (+1)
    return co2_rating(filtered, index + 1)


def oxygen_MAIN(lst):
    # raw result for oxygen
    oxygen_filtered_result = oxygen_rating(lst)
    # convert raw result into a decimal from binary
    oxygen_decimal_number = int(*oxygen_filtered_result, 2)
    return oxygen_decimal_number

def co2_MAIN(lst):
    # raw result for co2
    co2_filtered_result = co2_rating(lst)
    # convert raw result into a decimal from binary
    co2_decimal_number = int(*co2_filtered_result, 2)
    return co2_decimal_number


def ratings():
    with open('input_data.txt') as f:
        data = [row.strip() for row in f]
    
    oxygen = oxygen_MAIN(data)
    co2 = co2_MAIN(data)
    print(oxygen) 
    print(co2) 
    return oxygen * co2

print(ratings())