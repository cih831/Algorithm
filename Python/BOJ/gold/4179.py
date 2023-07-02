import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
miro = [list(input().strip()) for _ in range(R)]

answer = 0

q = deque()
for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            q.appendleft([i, j, 'J'])
            miro[i][j] = 0
        elif miro[i][j] == 'F':
            q.append([i, j, 'F'])

while q:
    x, y, char = q.popleft()
    if char == 'J' and miro[x][y] == 'F':
        continue

    if char == 'J' and (x == 0 or x == R - 1 or y == 0 or y == C - 1):
        answer = miro[x][y] + 1
        break

    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if char == 'J' and miro[nx][ny] == '.':
                miro[nx][ny] = miro[x][y] + 1
                q.append([nx, ny, 'J'])
            elif char == 'F' and not str(miro[nx][ny]) in 'F#':
                miro[nx][ny] = 'F'
                q.append([nx, ny, 'F'])

if not answer:
    answer = 'IMPOSSIBLE'

print(answer)