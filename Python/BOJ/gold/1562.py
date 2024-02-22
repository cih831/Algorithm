N = int(input())

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1 << 10):
            if j > 0:
                next = k | 1 << (j - 1)
                dp[i + 1][j - 1][next] += dp[i][j][k]
            if j < 9:
                next = k | 1 << (j + 1)
                dp[i + 1][j + 1][next] += dp[i][j][k]

result = 0
for i in range(10):
    result += dp[N][i][(1 << 10) - 1]
print(result % 1000000000)
