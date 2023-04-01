from collections import deque

N, M = map(int, input().split())
d = {}
for _ in range(N):
    k, v = map(int, input().split())
    d[k] = v

for _ in range(M):
    k, v = map(int, input().split())
    d[k] = v

board = [0] * 101
q = deque()
q.append(1)

while not board[100]:
    now = q.popleft()
    for dice in range(1, 7):
        if now + dice > 100:
            continue

        if not board[now + dice]:
            board[now + dice] = board[now] + 1
            if now + dice in d and not board[d[now + dice]]:
                board[d[now + dice]] = board[now] + 1
                q.append(d[now + dice])
            elif now + dice in d:
                continue
            else:
                q.append(now + dice)

print(board[100])