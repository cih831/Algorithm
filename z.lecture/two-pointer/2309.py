# small = [int(input()) for _ in range(9)]
# small.sort()
# s = sum(small)
# i = 0
# while len(small) > 7:
#     for j in range(i, 9):
#         if not i == j:
#             if s - small[i] - small[j] == 100:
#                 t1, t2 = small[i], small[j]
#                 small.remove(t1)
#                 small.remove(t2)
#                 break
#     i += 1
#
# for i in small:
#     print(i)


small = [int(input()) for _ in range(9)]
small.sort()
ssum = sum(small)
s = 0
e = 8

while s < e:
    if small[s] + small[e] == ssum - 100:
        t1, t2 = small[s], small[e]
        small.remove(t1)
        small.remove(t2)
        break
    elif small[s] + small[e] < ssum - 100:
        s += 1
    else:
        e -= 1

for i in small:
    print(i)