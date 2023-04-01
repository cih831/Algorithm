import sys
N, M, B = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    arr.extend(a)
arr.sort(reverse=True)
time = 10 ** 10
h = 0

for y in range(arr[-1], arr[0]+1):
    tmp = 0
    inven = B
    for i in range(N*M):
        if arr[i] > y:
            tmp += 2 * (arr[i] - y)
            inven += arr[i] - y
        else:
            tmp += y - arr[i]
            inven -= y - arr[i]
        if inven < 0:
            break
    if tmp <= time and inven >= 0:
        time = tmp
        h = y

print(time, h)