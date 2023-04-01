import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp_forward = [1 for _ in range(N)]
dp_backward = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j] and dp_forward[i] <= dp_forward[j]:
            dp_forward[i] = dp_forward[j] + 1
        if arr[N - 1 - i] > arr[N - 1 - j] and dp_backward[N - 1 - i] <= dp_backward[N - 1 - j]:
            dp_backward[N - 1 - i] = dp_backward[N - 1 - j] + 1

for i in range(N):
    arr[i] = dp_forward[i] + dp_backward[i]

print(max(arr) - 1)