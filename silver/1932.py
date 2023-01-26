import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

if N != 1:
    arr[1][1] += arr[0][0]

for i in range(N - 1):
    for j in range(len(arr[i])):
        if j != len(arr[i]) - 1:
            arr[i + 1][j + 1] += max(arr[i][j], arr[i][j + 1])
        if j == 0:
            arr[i + 1][0] += arr[i][j]
        elif j == len(arr[i]) - 1:
            arr[i + 1][j + 1] += arr[i][j]

print(max(arr[N - 1]))