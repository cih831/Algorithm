from collections import deque

N, M = map(int, input().split())

q = deque()
q.append([N, 1])
while q:
    x, cnt = q.popleft()
    if x == M:
        print(cnt)
        break
    for i in (x * 2, x * 10 + 1):
        if 0 <= i < M + 1:
            if i != M and i > M // 2:
                continue
            q.append([i, cnt + 1])
else:
    print(-1)