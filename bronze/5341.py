while True:
    N = int(input())
    if not N:
        break
    res = 0
    for i in range(1, N + 1):
        res += i
    print(res)