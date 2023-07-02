def recur(idx, ans, depth = 1):
    if depth == M:
        print(*ans)
        return
    for i in range(idx, L):
        recur(i, ans + [arr[i]], depth + 1)

N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
L = len(arr)
for i in range(L):
    recur(i, [arr[i]])