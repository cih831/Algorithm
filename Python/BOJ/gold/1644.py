N = int(input())

arr = [True] * (N + 1)
arr[0], arr[1] = False, False

for i in range(2, int(N**0.5) + 1):
    if arr[i] == True:
        for j in range(2, N // i + 1):
            arr[i * j] = False

p = [i for i in range(N + 1) if arr[i]]

s, e = 0, 0
cnt = 0

while s <= e and e < len(p):
    tmp = sum(p[s : e + 1])
    if tmp > N:
        s += 1
    else:
        if tmp == N:
            cnt += 1
        e += 1

print(cnt)
