import sys, heapq

input = sys.stdin.readline

N, M = map(int, input().split())

hq = []
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

for i in range(1, N + 1):
    if not in_degree[i]:
        heapq.heappush(hq, i)

while hq:
    now = heapq.heappop(hq)
    print(now, end=" ")

    for next in graph[now]:
        in_degree[next] -= 1
        if not in_degree[next]:
            heapq.heappush(hq, next)
