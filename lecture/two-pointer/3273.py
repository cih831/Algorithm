n = int(input())
li = list(map(int, input().split()))
li.sort()
print(li)
x = int(input())
cnt = 0
tmp = 0
s = 0
e = n-1

while s < e:
    tmp = li[s] + li[e]
    if tmp == x:
        cnt += 1
        e -= 1
    elif tmp < x:
        s += 1
    else:
        e -= 1

print(cnt)