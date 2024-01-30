import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
home, chicken = [], []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

chic_com_lst = list(combinations(chicken, M))
result = 1e9
for chic_com in chic_com_lst:
    result_tmp = 0
    for h in home:
        min_dist = 1e9
        for c in chic_com:
            min_dist = min(min_dist, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        result_tmp += min_dist
    result = min(result, result_tmp)

print(result)
