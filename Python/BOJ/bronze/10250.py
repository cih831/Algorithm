T = int(input())
for tc in range(1, T+1):
    H, W, N = map(int, input().split())

    x = str(N // H + 1)
    y = str(N % H)
    if y == '0':
        y = str(H)
        x = str(N // H)

    if len(x) == 1:
        print(y+'0'+x)
    else:
        print(y+x)