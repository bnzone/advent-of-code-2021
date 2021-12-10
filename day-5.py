def get_data():
    original_data = []
    with open('data_bnzone.txt') as f:
        max_left = 0
        max_right = 0
        for row in f:
            formatted = list(map(lambda coord: list(
                                    map(lambda part: int(part), coord.split(','))), row.split(' -> ')))
            original_data.append(formatted)
    return original_data


data = get_data()

"""Finding max number for the matrix columns, rows"""
max_num = 0
for row in data:
    for part in row:
        for num in part:
            if num > max_num:
                max_num = num

"""Matrix for storing intersections"""
graph = []
for row in range(max_num + 1):
    graph.append([0 for i in range(max_num + 1)])

"""Count all intersections"""
def get_count():
    count = 0
    for row in data:
        coord1, coord2 = row
        x1, y1 = coord1
        x2, y2 = coord2


        if y1 == y2:
            temp1 = x1
            while temp1 <= x2:
                graph[y1][temp1] += 1
                temp1 += 1
            temp2 = x1
            while temp2 >= x2:
                graph[y1][temp2] += 1
                temp2 -= 1

        elif x1 == x2:
            temp1 = y1
            while temp1 <= y2:
                graph[temp1][x1] += 1
                temp1 += 1
            temp2 = y1
            while temp2 >= y2:
                graph[temp2][x1] += 1
                temp2 -= 1

        #The 'else' statement below is needed to produce the answer for the Part 2 of the question
        else:
            # 9,7  ->  7,9
            if x1 > x2 and y1 < y2:
                temp_y = y1
                temp_x = x1

                while temp_y <= y2 and temp_x >= x2:
                    graph[temp_y][temp_x] += 1
                    temp_y += 1
                    temp_x -= 1
            # 7,9  ->  9,7
            elif x1 < x2 and y1 > y2:
                temp_y = y1
                temp_x = x1

                while temp_y >= y2 and temp_x <= x2:
                    graph[temp_y][temp_x] += 1
                    temp_y -= 1
                    temp_x += 1
            else:
                # 1,1 -> 3,3
                temp_y = y1
                temp_x = x1
                while temp_y <= y2 and temp_x <= x2:
                    graph[temp_y][temp_x] += 1
                    temp_y += 1
                    temp_x += 1
                # 3,3 -> 1,1

                temp_y2 = y1
                temp_x2 = x1
                while temp_y2 >= y2 and temp_x2 >= x2:
                    graph[temp_y2][temp_x2] += 1
                    temp_y2 -= 1
                    temp_x2 -= 1
                
    for row in graph:
        for num in row:
            if num > 1:
                count += 1
    return count

print(get_count())




