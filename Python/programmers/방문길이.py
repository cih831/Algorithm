def solution(dirs):
    answer = 0
    d = {'U': (-1, 0, 'D'), 'D': (1, 0, 'U'), 'R': (0, 1, 'L'), 'L': (0, -1, 'R')}
    visited = [[set() for _ in range(11)] for _ in range(11)]
    x, y = 5, 5

    for command in dirs:
        nx, ny = x + d[command][0], y + d[command][1]
        if 0 <= nx < 11 and 0 <= ny < 11:
            if not command in visited[x][y] or not d[command][2] in visited[nx][ny]:
                answer += 1
                visited[x][y].add(command)
                visited[nx][ny].add(d[command][2])
            x, y = nx, ny

    return answer

print(solution("ULURRDLLU"))