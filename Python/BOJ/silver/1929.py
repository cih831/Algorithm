N, M = map(int, input().split())

lst = [True for _ in range(M+1)]
lst[0] = lst[1] = False
for i in range(2, M+1):
    if not lst[i]:
        continue
    for j in range(i*i, M+1, i):
        lst[j] = False

for i in range(N, M+1):
    if lst[i]:
        print(i)