import sys
from collections import deque

input = sys.stdin.readline

def bfs(s):
    q = deque()
    q.append(s)
    visited = [-1] * (N + 1)
    visited[s] = 0

    while q:
        now = q.popleft()
        for i in range(0, len(graph[now])):
            if visited[graph[now][i][0]] == -1:
                visited[graph[now][i][0]] = visited[now] + graph[now][i][1]
                q.append(graph[now][i][0])
    
    return {'node': visited.index(max(visited)), 'distance': max(visited)}


N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    S, E, T = map(int, input().split())
    graph[S].append((E, T))
    graph[E].append((S, T))

print(bfs(bfs(1)['node'])['distance'])