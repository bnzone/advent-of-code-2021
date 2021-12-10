
prod_numbers = [42,44,71,26,70,92,77,45,6,18,79,54,31,34,64,32,16,55,81,11,90,10,21,87,0,84,8,23,1,12,60,20,57,68,61,82,49,59,22,2,63,33,50,39,28,30,88,41,69,72,98,73,7,65,53,35,96,67,36,4,51,75,24,86,97,85,66,29,74,40,93,58,9,62,95,91,80,99,14,19,43,37,27,56,94,25,83,48,17,38,78,15,52,76,5,13,46,89,47,3]

data = []

with open('input.txt') as f:
    board = []
    for row in f:
        good_row = list(map(lambda n: int(n), row.split()))
        if len(good_row):
            board.append(good_row)
        else:
            data.append(board)
            board = []
    data.append(board)

def check_x(board, current_numbers):
    for row in board:
        matches = 0
        for cell in row:
            if cell in current_numbers:
                matches += 1
        if matches == 5:
            return True
    return False

def check_y(board, current_numbers):
    for i in range(0, len(board[0])):
        matches = 0
        for row in board:
            if row[i] in current_numbers:
                matches +=1
        if matches == 5:
            return True
    return False

def check_boards(boards, current_numbers):
    won = []
    for idx, board in enumerate(boards):
        if check_x(board, current_numbers) or check_y(board, current_numbers):
            won.append(['bingo', board, idx])
    return won

def dealer(numbers, boards):
    shown = []
    win_indexes = []
    winner_boards = []
    num_ = None
    for num in numbers:
        shown.append(num)

        won_boards = check_boards(boards, shown)

        if len(won_boards) > 0:
            for winner in won_boards:
                idx = winner[2]
                board = winner[1]
                if idx not in win_indexes:
                    win_indexes.append(idx)
                    winner_boards.append(board)
                    num_ = num
    
    valid_nums = numbers[0: numbers.index(num_)+ 1]
    last_winner = winner_boards[-1]

    sum_ = 0
    for row in last_winner:
        for n in row:
            if n not in valid_nums:
                sum_ += n
    return sum_ * num_
    print(win_indexes)
    print(winner_boards)


print(dealer(prod_numbers, data))

    
