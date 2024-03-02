"""
프림
"""

# import sys, heapq

# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
# visited = [False] * (N + 1)

# for _ in range(M):
#     A, B, C = map(int, input().split())
#     graph[A].append((C, B))
#     graph[B].append((C, A))

# hq = [(0, 1)]
# cost_lst = []

# while hq and len(cost_lst) < N:
#     cost, now = heapq.heappop(hq)
#     if not visited[now]:
#         visited[now] = True
#         cost_lst.append(cost)

#         for w, v in graph[now]:
#             if not visited[v]:
#                 heapq.heappush(hq, (w, v))

# print(sum(cost_lst) - max(cost_lst))

"""
크루스칼
"""

import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

E = []
result = 0

for _ in range(M):
    E.append(tuple(map(int, input().split())))
E.sort(key=lambda x: x[2])

for e in E:
    A, B, C = e
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += C
        max_cost = C

print(result - max_cost)
