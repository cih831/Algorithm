import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, R = map(int, input().split())
item = [0] + list(map(int, input().split()))
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(R):
    s, e, t = map(int, input().split())
    dist[s][e] = t
    dist[e][s] = t

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

ans = 0
for i in range(1, N + 1):
    tmp = 0
    for j in range(1, N + 1):
        if dist[i][j] <= M or i == j:
            tmp += item[j]
    ans = max(ans, tmp)

print(ans)