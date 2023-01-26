a = []

cnt = 10

for i in range(10):
    a += [(int(input()))]

for i in range(10):
    a[i] = [a[i] % 42]

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        try:
            while a[i] == a[j]:
                cnt -= 1
                del a[j]
        except:
            break

print(cnt)