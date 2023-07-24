def solution(rows, columns, queries):
    answer = []
    arr = [[0] * columns] + [[0] + [j for j in range(i * columns + 1, i * columns + columns + 1)] for i in range(rows)]
    d = (0, 1), (1, 0), (0, -1), (-1, 0)

    for querie in queries:
        x1, y1, x2, y2 = querie
        x, y = x1, y1 + 1
        i = 0
        tmp = arr[x1][y1]
        min_num = arr[x1][y1]

        while True:
            min_num = min(min_num, arr[x][y])
            arr[x][y], tmp = tmp, arr[x][y]
            if (x + d[i][0] < x1 or x + d[i][0] > x2 or y + d[i][1] < y1 or y + d[i][1] > y2):
                i += 1
                if i == 4:
                    break
            x, y = x + d[i][0], y + d[i][1]
        
        answer.append(min_num)
    return answer

# def solution(rows, columns, queries):
#     answer = []
#     arr = [[0] * columns] + [[0] + [j for j in range(i * columns + 1, i * columns + columns + 1)] for i in range(rows)]

#     for querie in queries:
#         x1, y1, x2, y2 = querie
#         x, y = x1, y1 + 1
#         tmp = arr[x1][y1]
#         min_num = arr[x1][y1]
#         while y + 1 <= y2:
#             min_num = min(min_num, arr[x][y])
#             arr[x][y], tmp = tmp, arr[x][y]
#             y += 1
        
#         while x + 1 <= x2:
#             min_num = min(min_num, arr[x][y])
#             arr[x][y], tmp = tmp, arr[x][y]
#             x += 1

#         while y - 1 >= y1:
#             min_num = min(min_num, arr[x][y])
#             arr[x][y], tmp = tmp, arr[x][y]
#             y -= 1
        
#         while x - 1 >= x1 - 1:
#             min_num = min(min_num, arr[x][y])
#             arr[x][y], tmp = tmp, arr[x][y]
#             x -= 1
        
#         answer.append(min_num)
            
#     return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))