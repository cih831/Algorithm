import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().rstrip())))

visited = [[{'not_break': -1, 'break': -1} for _ in range(M)] for _ in range(N)]

q = deque()
q.append((N - 1, M - 1, 'not_break'))
visited[N - 1][M - 1]['not_break']= 1
while q:
    x, y, z = q.popleft()
    if (x, y) == (0, 0):
        print(visited[0][0][z])
        break

    for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][z] == -1:

            if arr[nx][ny] == 1 and z == 'not_break':
                visited[nx][ny]['break'] = visited[x][y][z] + 1
                q.append((nx, ny, 'break'))
            
            elif arr[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))

else:
    print(-1)

'''
6 4
0100
1110
1000
0000
0111
0000
ans: 15
----------
4 4
0111
1111
1111
1110
ans: -1
----------
2 4
0111
0110
ans: -1
----------
1 1
0
ans: 1
----------
5 8
01000000
01010000
01010000
01010011
00010010
ans: 20
----------
6 7
0000000
0111111
0100010
0101010
0101010
0001010
ans: 12
---------
8 8
01000100
01010100
01010100
01010100
01010100
01010100
01010100
00010100
ans: 29
----------
3 3
011
111
110
ans: -1
-----------
3 6
010000
010111
000110
ans: 12
-----------
3 3
000
000
000
ans: 5
----------
4 4
0101
0101
0001
1110
ans: 7
'''