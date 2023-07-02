import sys
input = sys.stdin.readline

T = int(input())

for tc in range(T):
    n = int(input())
    arr = []
    arr.append(list(map(int, input().split())))
    arr.append(list(map(int, input().split())))
    if n >= 2:
        dp = [[arr[0][0], arr[0][1] + arr[1][0]], [arr[1][0], arr[1][1] + arr[0][0]]]
    else:
        dp = [[arr[0][0]], [arr[1][0]]]

    for i in range(2, n):
        dp[0].append(arr[0][i] + max(dp[1][i - 2], dp[1][i - 1]))
        dp[1].append(arr[1][i] + max(dp[0][i - 2], dp[0][i - 1]))
    
    print(max(dp[0][n - 1], dp[1][n - 1]))