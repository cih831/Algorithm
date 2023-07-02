n = int(input())
sol = list(map(int, input().split()))
#
# a = b = 0
# mix = 2000000000
#
# for i in range(n):
#     for j in range(n-1, 0, -1):
#         if i != j and abs(sol[i]+sol[j]) < mix:
#             mix = abs(sol[i]+sol[j])
#             a, b = sol[i], sol[j]
#
# print(a, b)


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