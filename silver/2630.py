def paper_cut(n, x=0, y=0):
    a = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if a != arr[i][j]:
                for k in range(2):
                    for l in range(2):
                        paper_cut(n // 2, x + k * n // 2, y + l * n // 2)
                return
    cnt[a] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0]

paper_cut(N)

for i in range(2):
    print(cnt[i])
