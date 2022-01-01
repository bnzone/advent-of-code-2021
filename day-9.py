# PART 1

rows = []
with open('data.txt') as f:
    for row in f:  
        r = row.split('\n')[0]
        rows.append(r)

matrix = []

for number in rows:
    res = []
    for digit in number:
        res.append(int(digit))
    matrix.append(res)

low_points = []

for y, row in enumerate(matrix):
    for x, digit in enumerate(row):
        left = False
        right = False
        top = False
        bottom = False

        #check left
        if x == 0:
            left = True
        else:
            if matrix[y][x-1] > digit:
                left = True

        #check right
        if x == len(row) - 1:
            right = True
        else:
            if matrix[y][x + 1] > digit:
                right = True

        #check top
        if y == 0:
            top = True
        else:
            if matrix[y - 1][x]  > digit:
                    top = True

        #check bot
        if y == len(matrix) - 1:
            bottom = True
        else:
            if matrix[y + 1][x]  > digit:
                bottom = True

        if left and right and top and bottom:
            low_points.append(digit)

sum = 0
for num in low_points:
    sum += num + 1
print(sum)


