import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
dist = [[INF] * n for _ in range(n)]
for _ in range(m):
    s, e, t = map(int, input().split())
    if dist[s - 1][e - 1] > t:
        dist[s - 1][e - 1] = t

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()