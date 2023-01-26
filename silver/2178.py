from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

q = deque()
q.append([0, 0])
while q:
    x, y = q.popleft()
    if [x, y] == [N-1, M-1]:
        break
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and [nx, ny] != [0, 0]:
            q.append([nx, ny])
            arr[nx][ny] += arr[x][y]

print(arr[-1][-1])

