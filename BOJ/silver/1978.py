N = int(input())
num = list(map(int, input().split()))
num.sort()

lst = [True for _ in range(num[-1]+1)]
lst[0] = lst[1] = False
for i in range(2, num[-1]+1):
    if not lst[i]:
        continue
    for j in range(i*i, num[-1]+1, i):
        lst[j] = False

cnt = 0
for i in num:
    if lst[i]:
        cnt += 1

print(cnt)