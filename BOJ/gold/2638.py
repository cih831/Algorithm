import sys
from collections import deque
input = sys.stdin.readline

def recur(cheese, recur_cnt = 1):
    visited = [[0] * M for _ in range(N)]
    change_lst = []
    q = deque()
    q.append((0, 0))
    zero_cnt = 0

    while q:
        x, y = q.popleft()
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] >= 0:
                if cheese[nx][ny] == 1:
                    visited[nx][ny] += 1
                    if visited[nx][ny] == 2:
                        change_lst.append((nx, ny))
                else:
                    visited[nx][ny] = -1
                    q.append((nx, ny))
                    zero_cnt += 1

    for x, y in change_lst:
        cheese[x][y] = 0
        zero_cnt += 1

    if zero_cnt == N * M:
        return recur_cnt
    else:
        return recur(cheese, recur_cnt + 1)



N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

print(recur(arr))