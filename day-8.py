# PART 1

# decode_dict {number_consists_of_letters: corresponding_number}
unsorted_decoded_dict = {
    'acedgfb': 8,
    'cdfbe': 5,
    'gcdfa': 2,
    'fbcad': 3,
    'dab': 7,
    'cefabd': 9,
    'cdfgeb': 6,
    'eafb': 4,
    'cagedb': 0,
    'ab': 1
}


sorted_decoded_dict = {
    # 'abcdefg': 8, 
    'bcdef': 5, 
    'acdfg': 2, 
    'abcdf': 3, 
    # 'abd': 7, 
    'abcdef': 9, 
    'bcdefg': 6, 
    # 'abef': 4, 
    'abcdeg': 0, 
    # 'ab': 1
}


input = []
with open('input.txt') as f:
    for row in f:
        divided = row.split(' | ')
        right_part_list = divided[1].split()
        input.append(right_part_list)

count = 0

for row in input: 
    code = []
    for word in row:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in sorted_decoded_dict:
            code.append(str(sorted_decoded_dict[sorted_word]))
        else:
            if len(sorted_word) == 2:
                code.append('1')
            elif len(sorted_word) == 4:
                code.append('4')
            elif len(sorted_word) == 3:
                code.append('7')
            elif len(sorted_word) == 7:
                code.append('8')
    string_number = ''.join(code)
    count += int(string_number)


print(count)
