def dfs(V):
    visited[V] = 1
    print(V, end=' ')
    for n in arr[V]:
        if not visited[n]:
            dfs(n)

def bfs(V):
    q = [V]
    visited[V] = 1
    while q:
        n = q.pop(0)
        print(n, end=' ')
        for i in arr[n]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in E:
    arr[i[0]].append(i[1])
    arr[i[1]].append(i[0])
for i in range(N+1):
    arr[i].sort()
dfs(V)
print()
visited = [0]*(N+1)
bfs(V)