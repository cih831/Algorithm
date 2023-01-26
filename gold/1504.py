import heapq
import sys

input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))
v1, v2 = map(int, input().split())
inf = int(1e9)

def dijkstra(s):
  q = []
  heapq.heappush(q, (0, s))
  distance = [inf] * (N + 1)
  distance[s] = 0
  
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    else:
      for next in graph[node]:
        cost = distance[node] + next[1]
        if cost < distance[next[0]]:
          distance[next[0]] = cost
          heapq.heappush(q, (cost, next[0]))

  return distance

start = dijkstra(1)
v1_start = dijkstra(v1)
v2_start = dijkstra(v2)
result = min(start[v1] + v1_start[v2] + v2_start[N], start[v2] + v2_start[v1] + v1_start[N])

print(result if result < inf else -1)