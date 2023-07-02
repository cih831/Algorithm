import heapq
import sys
input = sys.stdin.readline

def dijkstra(s):
  q = []
  heapq.heappush(q, (0, s))
  distance = [inf] * (V + 1)
  distance[s] = 0

  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for next in graph[node]:
      cost = distance[node] + next[1]
      if cost < distance[next[0]]:
        distance[next[0]] = cost
        heapq.heappush(q, (cost, next[0]))
    
  return distance

V, E = map(int, input().split())
K = int(input())
inf = int(1e9) 
graph = [[] for _ in range(V + 1)]
for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

distance = dijkstra(K)

for i in range(1, V + 1):
  print(distance[i] if distance[i] != inf else 'INF')