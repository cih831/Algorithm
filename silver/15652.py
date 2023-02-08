def recur(nums):
    if len(nums) == M:
        print(*nums)
        return
    for i in range(nums[-1], N + 1):
        recur(nums + [i])

N, M = map(int, input().split())
for i in range(1, N + 1):
    recur([i])