N = int(input())
p = [1, 2]
for i in range(2, N):
    p.append(p[i-2] + p[i-1])

if N == 1:
    print(p[0])
else:
    print(p[-1] % 10007)