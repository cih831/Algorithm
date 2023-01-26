def dfs(x, y, idx, total):
    global ans
    if ans >= total + my_max * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if idx == 1:
                    visit[nx][ny] = 1
                    dfs(x, y, idx + 1, total + arr[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, idx + 1, total + arr[nx][ny])
                visit[nx][ny] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [([0] * M) for _ in range(N)]
ans = 0
my_max = 0
for ar in arr:
    my_max = max(my_max, max(ar))

for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        dfs(i, j, 0, arr[i][j])
        visit[i][j] = 0

print(ans)