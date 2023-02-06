import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])
S, E = map(int, input().split())

q = []
heapq.heappush(q, (0, S))
d = [INF] * (N + 1)
d[S] = 0
route = [[S] for _ in range(N + 1)]
while q:
    dist, node = heapq.heappop(q)
    if d[node] < dist:
        continue
    for next in graph[node]:
        cost = d[node] + next[1]
        if cost < d[next[0]]:
            d[next[0]] = cost
            route[next[0]] = node
            heapq.heappush(q, (cost, next[0]))

ans = [E]
for _ in range(N + 1):
    ans = [route[ans[0]]] + ans
    if ans[0] == S:
        break
print(d[E])
print(len(ans))
print(*ans)