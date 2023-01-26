def dfs(n, x=0, y=0):
    global cnt
    num = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        dfs(n // 3, x + k * n // 3, y + l * n // 3)
                return
    cnt[num] += 1


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = [0, 0, 0]

dfs(N)
for i in range(-1, 2):
    print(cnt[i])