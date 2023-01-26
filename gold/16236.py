from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0]*N for _ in range(N)]
q = deque()
bs = 2
cnt = 0
time = 0

for x in range(N):
    for y in range(N):
        if arr[x][y] == 9:
            q.append([x, y])
            arr[x][y] = 0
            visited[x][y] = 1

while q:
    x, y = q.popleft()
    if 0 < arr[x][y] < bs:
        for i in range(N):
            for j in range(N):
                if visited[x][y] == visited[i][j] and 0 < arr[i][j] < bs:
                    x, y = i, j
                    break
            if x == i and y == j:
                break
        cnt += 1
        arr[x][y] = 0
        time += visited[x][y] - 1
        visited = [[0]*N for _ in range(N)]
        visited[x][y] = 1
        q = deque()
        if cnt == bs:
            bs += 1
            cnt = 0

    for dx, dy in (-1, 0), (0, -1), (0, 1), (1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] <= bs and not visited[nx][ny]:
            q.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1

print(time)