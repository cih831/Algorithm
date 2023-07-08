import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * m for _ in range(n)]

target = False
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            target = (i, j)
        if target:
            break
    if target:
        break

q = deque()
q.append(target)
while q:
    x, y = q.popleft()
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if (
            0 <= nx < n
            and 0 <= ny < m
            and not arr[nx][ny] in (2, 0)
            and not ans[nx][ny]
        ):
            ans[nx][ny] = ans[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and ans[i][j] == 0:
            ans[i][j] = -1

for item in ans:
    print(*item)
