N, r, c = map(int, input().split())
tmp = 0
while N > 1:
    s = 0
    e = 2**(N*2)
    if r < 2**(N - 1) <= c: # 1 사분면
        c -= 2**(N-1)
        s = e//4
        e = e//2
    elif r < 2**(N-1) and c < 2**(N-1): # 2 사분면
        e = e//4
    elif r >= 2**(N - 1) > c: # 3 사분면
        r -= 2**(N-1)
        s = e//2
        e = e//4*3
    else: # 4 사분면
        r -= 2**(N-1)
        c -= 2**(N-1)
        s = e//4*3
    N -= 1
    tmp += s
if not r and not c:
    tmp += 0
elif not r and c:
    tmp += 1
elif r and not c:
    tmp += 2
else:
    tmp += 3
print(tmp)