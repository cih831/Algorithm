import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0]*M for _ in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        arr[y][x] = 1
    cnt = 0
    q = deque()
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                cnt += 1
                arr[i][j] = 0
                q.append([i, j])
                while q:
                    y, x = q.popleft()
                    for k in range(4):
                        dy = y + di[k]
                        dx = x + dj[k]
                        if 0 <= dy < N and 0 <= dx < M and arr[dy][dx]:
                            q.append([dy, dx])
                            arr[dy][dx] = 0
    print(cnt)