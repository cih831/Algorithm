from collections import deque

def bfs(start):
  visited = [-1] * (N + 1)
  q = deque()
  q.append(start)
  visited[start] = 0

  while q:
    now = q.popleft()
    for i in range(0, len(V[now]), 2):
      if visited[V[now][i]] == -1:
        visited[V[now][i]] = visited[now] + V[now][i + 1]
        q.append(V[now][i])

  result = {'node': visited.index(max(visited)), 'distance': max(visited)}
  return result


N = int(input())

V = [[]] * (N + 1)
for v in range(N):
  tmp = list(map(int, input().split()))
  V[tmp[0]] = tmp[1:-1]

print(bfs(bfs(1)['node'])['distance'])