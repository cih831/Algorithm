import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

tmp = 1
for i in range(2, V + 1):
    if len(graph[i]) < len(graph[tmp]):
        tmp = i

h = [(0, tmp)]
visited = [0] * (V + 1)
result = 0
while h:
    w, now = heapq.heappop(h)
    if not visited[now]:
        visited[now] = 1
        result += w

        for next, next_w in graph[now]:
            heapq.heappush(h, (next_w, next))

print(result)
