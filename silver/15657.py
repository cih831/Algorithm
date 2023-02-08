def recur(idx, ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(idx, N):
        recur(i, ans + [arr[i]])
    

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
for i in range(N):
    recur(i, [arr[i]])