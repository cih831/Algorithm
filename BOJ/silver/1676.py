N = int(input())
res = 1
while N:
    res *= N
    N -= 1
res = str(res)
for i in range(1, len(res)+1):
    if int(res[-i]):
        print(i-1)
        break