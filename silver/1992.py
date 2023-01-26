def div(n, a=0, b=0):
    global ans
    x = arr[a][b]
    for i in range(a, a+n):
        for j in range(b, b+n):
            if x != arr[i][j]:
                ans += '('
                for k in range(2):
                    for l in range(2):
                        div(n//2, a+n//2*k, b+n//2*l)
                ans += ')'
                return
    else:
        ans += str(x)


N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = ''
div(N)
print(ans)