def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n + 1)] # 삼각형 모양 만들기
    d = (1, 0), (0, 1), (-1, -1)
    x, y = 0, 0
    status = 0
    for i in range(1, sum(num for num in range(n + 1)) + 1):
        arr[x][y] = i
        status_ = status % 3
        nx, ny = x + d[status_][0], y + d[status_][1]
        if 0 <= nx < n and 0 <= ny <= nx and not arr[nx][ny]:
            x, y = nx, ny
        else: # 방향전환
            status += 1
            status_ = status % 3
            x, y = x + d[status_][0], y + d[status_][1]
    
    for item in arr:
        answer.extend(item)

    return answer

print(solution(5))