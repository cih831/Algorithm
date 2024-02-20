import sys
from itertools import combinations

input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
tmp = [arr[: N // 2], arr[N // 2 :]]
com_sum = [{S: 0}, {S: 0}]
for i in range(2):
    for j in range(1, len(tmp[i]) + 1):
        for com in combinations(tmp[i], j):
            if sum(com) in com_sum[i]:
                com_sum[i][sum(com)] += 1
            else:
                com_sum[i][sum(com)] = 1

result = com_sum[0][S] + com_sum[1][S]

for s1 in com_sum[0]:
    if S - s1 in com_sum[1]:
        result += com_sum[0][s1] * com_sum[1][S - s1]

print(result)
