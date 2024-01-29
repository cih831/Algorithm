import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(N)]

q = deque()
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == "I":
            q.append((i, j))
            break
    if q:
        break

while q:
    x, y = q.popleft()
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny] in "IXV":
            if arr[nx][ny] == "P":
                cnt += 1
            q.append((nx, ny))
            arr[nx][ny] = "V"

print(cnt if cnt else "TT")
