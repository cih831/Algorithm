from collections import deque

S, E = map(int, input().split())
M = max(S, E)
visited = [0] * (M + 1)
before = [0] * (M + 1)

q = deque()
q.append(S)
while q:
    now = q.popleft()
    if now == E:
        break
    for i in (now - 1, now + 1, now * 2):
        if 0 <= i <= M and not visited[i]:
            visited[i] = visited[now] + 1
            before[i] = now
            q.append(i)

ans = [E]
for i in range(visited[E]):
    ans.append(before[ans[-1]])

print(visited[E])
print(' '.join(map(str, ans[::-1])))