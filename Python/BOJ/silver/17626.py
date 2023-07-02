N = int(input())
ans = 0

while 1:
    if N ** 0.5 == int(N ** 0.5):
        ans = 1
    if ans:
        break
    for i in range(1, int(N**0.5) + 1):
        if int((N - i**2)**0.5) == (N - i**2)**0.5:
            ans = 2
    if ans:
        break
    for i in range(1, int(N**0.5) + 1):
        for j in range(1, int((N - i**2)**0.5) + 1):
            if int((N - i**2 - j**2)**0.5) == (N - i**2 - j**2)**0.5:
                ans = 3
    if ans:
        break
    ans = 4
    break

print(ans)