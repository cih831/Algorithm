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
