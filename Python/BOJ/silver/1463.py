from collections import deque

N = int(input())
visited = [0] * (N+1)
q = deque()
q.append(N)
while q:
    x = q.popleft()
    if x == 1:
        print(visited[1])
        break
    if not x % 3 and not visited[x//3]:
        q.append(x//3)
        visited[x//3] = visited[x] + 1
    if not x % 2 and not visited[x//2]:
        q.append(x//2)
        visited[x//2] = visited[x] + 1
    if not visited[x-1]:
        q.append(x-1)
        visited[x-1] = visited[x] + 1
