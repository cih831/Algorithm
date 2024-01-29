import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    lst = input().split()
    if N > 32:
        print(0)
        continue

    for i in range(N):
        tmp = "0b"
        for s in lst[i]:
            if s in "ESTJ":
                tmp += "0"
            else:
                tmp += "1"
        lst[i] = int(tmp, 2)

    graph = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            graph[i][j] = bin(lst[i] ^ lst[j]).count("1")

    min_dist = int(1e9)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                min_dist = min(min_dist, graph[i][j] + graph[i][k] + graph[j][k])

    print(min_dist)
