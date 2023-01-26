K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]
s = 1
e = max(L)

while s <= e:
    c = (s+e)//2
    cnt = 0
    for i in L:
        cnt += i // c

    if cnt >= N:
        s = c + 1
    else:
        e = c - 1

print(e)