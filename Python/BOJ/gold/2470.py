n = int(input())
sol = list(map(int, input().split()))
sol.sort()

s = 0
e = n-1
a = sol[0]
b = sol[-1]

while s < e:
    if abs(sol[s]+sol[e]) < abs(a+b):
        a, b = sol[s], sol[e]

    if sol[s] + sol[e] < 0:
        s += 1
    else:
        e -= 1

print(a, b)