import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
gem = [tuple(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
gem.sort()
bag.sort()
result, tmp = 0, []

for b in bag:
    while gem and gem[0][0] <= b:
        heapq.heappush(tmp, -gem[0][1])
        heapq.heappop(gem)
    if tmp:
        result -= heapq.heappop(tmp)

print(result)
