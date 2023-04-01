from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
ans = 0
my_max = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j])

while q:
    x, y = q.popleft()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            arr[nx][ny] = arr[x][y] + 1
            my_max = max(my_max, arr[nx][ny])
            q.append([nx, ny])

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            ans = -1
            break
    if ans == -1:
        break
else:
    ans = my_max - 1

print(ans)