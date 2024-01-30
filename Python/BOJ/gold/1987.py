import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = list(input().rstrip() for _ in range(R))
max_cnt = 1


def DFS(x=0, y=0, visited=board[0][0], cnt=1):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in visited:
            DFS(nx, ny, visited + board[nx][ny], cnt + 1)


DFS()
print(max_cnt)

# BFS(시간, 메모리 초과)
# import sys
# from collections import deque

# input = sys.stdin.readline

# R, C = map(int, input().split())
# board = list(input().rstrip() for _ in range(R))
# q = deque([(0, 0, board[0][0], 1)])
# max_cnt = 0

# while q:
#     x, y, visited, cnt = q.popleft()
#     max_cnt = max(max_cnt, cnt)
#     for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
#         nx, ny = x + dx, y + dy
#         if 0 <= nx < R and 0 <= ny < C and not board[nx][ny] in visited:
#             q.append((nx, ny, visited + board[nx][ny], cnt + 1))

# print(cnt)
