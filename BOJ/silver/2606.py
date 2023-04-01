from collections import deque

N = int(input())
V = int(input())
a = [[] for _ in range(N+1)]
# b = [[] for _ in range(N)]

for i in range(V):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)

q = deque()
q.append(1)
visited = [0]*(N+1)
visited[1] = 1
cnt = 0
while q:
    x = q.popleft()
    for com in a[x]:
        if not visited[com]:
            q.append(com)
            visited[com] = 1
            cnt += 1

print(cnt)