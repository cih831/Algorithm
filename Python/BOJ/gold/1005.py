import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    in_degree = [0] * (N + 1)
    dp = [0] * (N + 1)
    E = [[] for _ in range(N + 1)]
    for _ in range(K):
        x, y = map(int, input().split())
        E[x].append(y)
        in_degree[y] += 1
    W = int(input())

    q = deque()
    for i in range(1, N + 1):
        if not in_degree[i]:
            q.append(i)
            dp[i] = D[i]

    while q:
        now = q.popleft()
        for next in E[now]:
            in_degree[next] -= 1
            dp[next] = max(dp[now] + D[next], dp[next])
            if not in_degree[next]:
                q.append(next)

    print(dp[W])


"""
역순 BFS 풀이


import sys

from collections import deque

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    time = [0] * (N + 1)
    E = [[] for _ in range(N + 1)]
    for _ in range(K):
        x, y = map(int, input().split())
        E[y].append(x)
    W = int(input())
    time[W] = D[W]

    q = deque()
    q.append(W)

    while q:
        now = q.popleft()
        for next in E[now]:
            if time[next] < time[now] + D[next]:
                time[next] = time[now] + D[next]
                q.append(next)

    print(max(time))
"""
