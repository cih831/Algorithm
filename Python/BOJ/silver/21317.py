import sys
from copy import deepcopy
input = sys.stdin.readline

def rock(dp_tmp, idx):
    # print(idx)
    dp_tmp[idx] = dp_tmp[idx - 3] + super_jump
    if idx < N - 1:
        dp_tmp[idx + 1] = dp_tmp[idx] + arr[idx][0]
        for i in range(idx + 2, N):
            dp_tmp[i] = min(dp_tmp[i - 2] + arr[i - 2][1], dp_tmp[i - 1] + arr[i - 1][0])
    # print(idx, dp_tmp)
    return dp_tmp

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N - 1)]
super_jump = int(input())
dp = [0] * N
if N > 1:
    dp[1] = arr[0][0]

    for i in range(2, N):
        dp[i] = min(dp[i - 2] + arr[i - 2][1], dp[i - 1] + arr[i - 1][0])

    # print(dp)
    my_min = dp[-1]
    for i in range(3, N):
        # print(dp)
        # print(rock(dp, i))
        my_min = min(my_min, rock(deepcopy(dp), i)[-1])
else:
    my_min = 0

print(my_min)