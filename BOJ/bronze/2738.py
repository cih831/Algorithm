N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

lst = []

for i in range(N):
    tmp = []
    for j in range(M):
        tmp.append(A[i][j] + B[i][j])
    lst.append(tmp)

for i in range(N):
    print(*lst[i])