from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque()
ans = 0
my_max = 1

for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append([i, j, k])

while q:
    x, y, z = q.popleft()
    for dx, dy, dz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and not arr[nx][ny][nz]:
            arr[nx][ny][nz] = arr[x][y][z] + 1
            my_max = max(my_max, arr[nx][ny][nz])
            q.append([nx, ny, nz])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if not arr[i][j][k]:
                ans = -1
                break
        if ans == -1:
            break
    if ans == -1:
        break
else:
    ans = my_max - 1

print(ans)