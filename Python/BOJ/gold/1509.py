S = input()
L = len(S)

dp = [int(1e9)] * L
dp[0] = 1
p = [[1 if i == j else 0 for j in range(L)] for i in range(L)]

for i in range(L - 1):
    if S[i] == S[i + 1]:
        p[i][i + 1] = 1

for e in range(L):
    for s in range(e):
        if S[s] == S[e] and p[s + 1][e - 1]:
            p[s][e] = 1

for e in range(1, L):
    for s in range(e):
        if p[s][e]:
            if s == 0:
                dp[e] = 1
            else:
                dp[e] = min(dp[e - 1] + 1, dp[s - 1] + 1, dp[e])
    else:
        dp[e] = min(dp[e], dp[e - 1] + 1)

print(dp[-1])
