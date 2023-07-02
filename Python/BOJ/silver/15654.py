def NM(arr, idx):
    if len(arr) == M:
        print(*arr)
        return        
    for j in range(0, N):
        if not nums[j] in arr:
            NM(arr + [nums[j]], j)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for i in range(0, N):
    NM([nums[i]], i)