def recur(ans, vis):
    if len(ans) == M:
        print(*ans)
        return
    tmp = 0
    for i in range(N):
        if vis[i] or arr[i] == tmp:
            continue
        vis[i] = 1
        tmp = arr[i]
        recur(ans + [arr[i]], vis)
        vis[i] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for i in range(N):
    if i > 0 and arr[i] == arr[i - 1]:
        continue
    visited = [0] * N
    visited[i] = 1
    recur([arr[i]], visited)