import sys
input = sys.stdin.readline

def recur(arr, m):
    tmp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp[i][j] += arr[i][k] * arr[k][j]
            tmp[i][j] %= 1000

    if m > 3:
        tmp = recur(tmp, m//2)
    if m % 2:
        res = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    res[i][j] += tmp[i][k] * arr[k][j]
                res[i][j] %= 1000
    else:
        res = tmp
    return res


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

if M == 1:
    res = arr
    for i in range(len(res)):
        for j in range(len(res[i])):
            res[i][j] %= 1000
else:
    res = recur(arr, M)

for row in res:
    print(*row)