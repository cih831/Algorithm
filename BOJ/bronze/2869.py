import sys

A, B, V = map(int, sys.stdin.readline().split())
# t = tot = 0
#
# while 1:
#     t += 1
#     tot += A
#     if tot >= V:
#         break
#     else:
#         tot -= B
#
# print(t)

t = (V-A) // (A-B)
if (V-A) % (A-B):
    print(t+2)
else:
    print(t+1)