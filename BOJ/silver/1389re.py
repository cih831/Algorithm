import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
kavin = int(1e9)
inssa = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N + 1):
    q = deque()
    q.append(i)
    visited = [0] * (N + 1)
    while q:
        now = q.popleft()
        for friend in graph[now]:
            if not visited[friend] and i != friend:
                visited[friend] = visited[now] + 1
                q.append(friend)

    if sum(visited) < kavin:
        kavin = sum(visited)
        inssa = i

print(inssa)