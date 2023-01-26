from collections import deque

def bfs(a, b):
    global visited, cnt1
    q = deque()
    visited[a][b] = 1
    q.append([a, b])
    target = arr[a][b]
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == target:
                visited[nx][ny] = 1
                q.append([nx, ny])
    cnt1 += 1


def bfs2(a, b):
    global visited, cnt2
    q = deque()
    visited[a][b] = 1
    q.append([a, b])
    if arr[a][b] in 'RG':
        target = 'RG'
    else:
        target = 'B'
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] in target:
                visited[nx][ny] = 1
                q.append([nx, ny])
    cnt2 += 1

N = int(input())
arr = [list(map(str, input())) for _ in range(N)]
cnt1 = cnt2 = 0
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs2(i, j)

print(cnt1, cnt2)