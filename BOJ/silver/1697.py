from collections import deque

N, K = map(int, input().split())
q = deque()
visited = [0]*100001
q.append(N)
while q:
    x = q.popleft()
    if x == K:
        print(visited[x])
        break
    if x + 1 <= 100000 and not visited[x+1]:
        q.append(x+1)
        visited[x+1] = visited[x] + 1
    if x - 1 >= 0 and not visited[x-1]:
        q.append(x-1)
        visited[x-1] = visited[x] + 1
    if x * 2 <= 100000 and not visited[x*2]:
        q.append(x*2)
        visited[x*2] = visited[x] + 1