import sys

N = int(input())
lst = [int(sys.stdin.readline()) for _ in range(N)] + [0]*2
dp = [0] * (N+2)

dp[0] = lst[0]
dp[1] = lst[0] + lst[1]
dp[2] = max(lst[1] + lst[2], lst[0] + lst[2])

for i in range(3, N):
    dp[i] = max(dp[i-3] + lst[i-1] + lst[i], dp[i-2] + lst[i])
print(dp[N-1])



















# 시간초과
# def max_score(arr, n=1):
#     global score
#     if n == N+1:
#         score[-1] = max(score[-1], arr[-1])
#         return
#     if not arr[n-1] or not arr[n-2]:
#         arr[n] = arr[n-1] + lst[n]
#         max_score(arr, n+1)
#         arr[n] = 0
#     if n + 1 <= N:
#         arr[n+1] = arr[n-1] + lst[n+1]
#         max_score(arr, n+2)
#         arr[n+1] = 0
#
#
#
# N = int(input())
# lst = [0] + [int(sys.stdin.readline()) for _ in range(N)]
# score = [0]*(N+1)
# tmp = [0]*(N+1)
# max_score(tmp)
#
# print(score[-1])