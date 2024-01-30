import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]  # status: [가로, 세로, 대각선]
dp[0][1][0] = 1
d = ((0, 1), (1, 0), (1, 1))

for x in range(N):
    for y in range(1 if x == 0 else 0, N):
        for m in range(3):
            nx, ny = x + d[m][0], y + d[m][1]
            if (
                nx < N
                and ny < N
                and graph[nx][ny] != 1
                and (m != 2 or not 1 in (graph[nx - 1][ny], graph[nx][ny - 1]))
            ):
                if m == 2:
                    dp[nx][ny][m] += sum(dp[x][y])
                else:
                    dp[nx][ny][m] += dp[x][y][m] + dp[x][y][2]

print(sum(dp[N - 1][N - 1]))
