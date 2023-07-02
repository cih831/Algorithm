def hanoi(n, s=1, e=3):
    if not n:
        return
    hanoi(n - 1, s, 6 - s - e)
    move.append([s, e])
    hanoi(n - 1, 6 - s - e, e)

move = []
hanoi(int(input()))
print(len(move))
for m in move:
    print(*m)

"""
[[321], [], []]
hanoi(3, 1, 3)
    hanoi(2, 1, 2)
        hanoi(1, 1, 3)
            hanoi(0, 1, 2)
            [1, 3] [[32], [], [1])
            hanoi(0, 2, 3)
        [1, 2] [[3][2][1]]
        hanoi(1, 3, 2)
            hanoi(0 ~~)
            [3, 2] [[3][21][]]
            hanoi(0 ~~)
    [1, 3] [[][21][3]]
    hanoi(2, 2, 3)
"""

"""
시간초과 bfs
from collections import deque
from copy import deepcopy

n = int(input())
arr = [[i for i in range(n, 0, -1)], [], []]
visited = [arr]
ans = [[], [], [i for i in range(n, 0, -1)]]

q = deque()
q.append([arr, []])
while q:
    now, move = q.popleft()

    if now == ans:
        print(len(move))
        for m in move:
            print(*m)

    for i in range(3): # 출발
        for j in range(3): # 도착
            tmp = deepcopy(now)
            if i != j and tmp[i] and (not tmp[j] or tmp[i][-1] < tmp[j][-1]): # 출발 도착이 다르고 출발지점에 원판이 있고, 옮기는 조건이 맞으면
                tmp[j].append(tmp[i].pop())
                if not tmp in visited:
                    visited.append(tmp)
                    q.append([tmp, move + [[i + 1, j + 1]]])
"""