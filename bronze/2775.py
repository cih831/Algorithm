T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())
    z = [i for i in range(1, n+1)]
    cnt = 0

    while cnt < k:
        for i in range(n-1, -1, -1):
            p = 0
            for j in range(i+1):
                p += z[j]
            z[i] = p
        cnt += 1

    print(z[-1])