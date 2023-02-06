from collections import deque

S, E = map(int, input().split())

visited = [-1] * 100001
visited[S] = 0
cnt = 0

q = deque()
q.append(S)
while q:
    now = q.popleft()
    # print(now)
    if now == E:
        cnt += 1
        continue
    if 0 <= now - 1 < 100001 and (visited[now - 1] == -1 or visited[now] + 1 == visited[now - 1]):
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)
    if 0 <= now + 1 < 100001 and (visited[now + 1] == -1 or visited[now] + 1 == visited[now + 1]):
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)
    if 0 <= now * 2 < 100001 and (visited[now * 2] == -1 or visited[now] + 1 == visited[now * 2]):
        visited[now * 2] = visited[now] + 1
        q.append(now * 2)

print(visited[E])
print(cnt)