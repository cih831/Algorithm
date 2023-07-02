import sys
import heapq

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance = [inf] * (N + 1)
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

input = sys.stdin.readline
inf = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    S, E, T = map(int, input().split())
    graph[S].append((E, T))

s, e = map(int, input().split())

print(dijkstra(s)[e])