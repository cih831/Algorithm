from collections import deque
import sys

def bfs():
    q = deque()
    q.append([A, ''])

    while q:
        x, y = q.popleft()
        # D
        nx = x * 2 % 10000
        if not visited[nx]:
            if nx == B: return y + 'D'
            visited[nx] = 1
            q.append([nx, y + 'D'])
        # S
        nx = x - 1
        if nx == -1:
            nx = 9999
        if not visited[nx]:
            if nx == B: return y + 'S'
            visited[nx] = 1
            q.append([nx, y + 'S'])
        # L
        nx = (x % 1000) * 10 + (x // 1000)
        if not visited[nx]:
            if nx == B: return y + 'L'
            visited[nx] = 1
            q.append([nx, y + 'L'])
        # R
        nx = (x % 10) * 1000 + (x // 10)
        if not visited[nx]:
            if nx == B: return y + 'R'
            visited[nx] = 1
            q.append([nx, y + 'R'])


T = int(sys.stdin.readline())
for tc in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    visited = [0]*10000
    visited[A] = 1

    print(bfs())