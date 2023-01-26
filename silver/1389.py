def bfs(p):
    global my_min, people
    q = [[p, 0]]
    visited = [[1, 0]] + [[0, 0] for _ in range(N)]
    visited[p][0] = 1
    while q:
        x, y = q.pop(0)
        for r in rs[x]:
            if not visited[r][0]:
                visited[r][0], visited[r][1] = 1, y + 1
                q.append([r, y+1])
    cnt = 0
    for f in visited:
        cnt += f[1]
    if cnt < my_min:
        people = p
        my_min = cnt


N, M = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(M)]
rs = [set() for _ in range(N+1)]
my_min = 500000
people = 1
for relation in friends:
    rs[relation[0]].add(relation[1])
    rs[relation[1]].add(relation[0])
for num in range(1, N+1):
    bfs(num)
print(people)