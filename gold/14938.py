import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, R = map(int, input().split())
item = list(map(int, input().split()))
graph = [[] for _ in range(N)]
dist = [[INF * N] for _ in range(N)]

for _ in range(N):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])
    graph[e].append([s, t])
    dist[s][e] = t
    dist[e][s] = t

for i in range(N):
    for j in range(N):
        if i != j:
            pass