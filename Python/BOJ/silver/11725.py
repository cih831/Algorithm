import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
visited[1] = -1
for _ in range(N - 1):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

q = deque()
q.append(1)
while q:
    x = q.popleft()
    for node in E[x]:
        if not visited[node]:
            q.append(node)
            visited[node] = x

for i in range(2, N + 1):
    print(visited[i])
