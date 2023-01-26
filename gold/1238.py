from collections import deque

def dfs(direction):
  visited = [-1] * (N + 1)

  q = deque()
  q.append(X)
  visited[X] = 0

  while q:
    now = q.popleft()
    if direction == 1:
      for item in forward[now]:
        if visited[item[0]] == -1 or visited[item[0]] > visited[now] + item[1]:
          visited[item[0]] = visited[now] + item[1]
          q.append(item[0])

    else:
      for item in backward[now]:
        if visited[item[0]] == -1 or visited[item[0]] > visited[now] + item[1]:
          visited[item[0]] = visited[now] + item[1]
          q.append(item[0])
  
  return visited
    

N, M, X = map(int, input().split())

forward =  list([] for _ in range(N + 1))
backward = list([] for _ in range(N + 1))

for _ in range(M):
  A, B, T = map(int, input().split())
  forward[A].append([B, T])
  backward[B].append([A, T])

f_visited = dfs(1)
b_visited = dfs(-1)
my_max = 0

for i in range(N + 1):
  my_max = max(my_max, f_visited[i] + b_visited[i])

print(my_max)