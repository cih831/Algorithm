def NM(arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(arr[-1] + 1, N + 1):
        NM(arr + [i])

N, M = map(int, input().split())

for i in range(1, N - M + 2):
    NM([i])