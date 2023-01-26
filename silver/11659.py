import sys

input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))
num_sum = [0]
tot = 0

for i in range(N):
    tot += num[i]
    num_sum += [tot]

for _ in range(M):
    x, y = map(int, input().split())
    print(num_sum[y] - num_sum[x-1])