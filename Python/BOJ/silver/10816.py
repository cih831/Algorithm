import sys
from collections import Counter
N = int(sys.stdin.readline())
lstN = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
lstM = list(map(int, sys.stdin.readline().split()))
arr = [0]*M

cnt = Counter(lstN)
for i in range(M):
    if lstM[i] in cnt:
        arr[i] = cnt[lstM[i]]

print(*arr)

# for i in range(M):
#     if arr[i]:
#         continue
#     s = 0
#     e = N - 1
#     while s <= e:
#         m = (s+e) // 2
#         if lstM[i] == lstN[m]:
#             s = e = m
#             while lstN[s] == lstM[i]:
#                 s -= 1
#             while e < N and lstN[e] == lstM[i]:
#                 e += 1
#             arr[i] = e - s - 1
#             for j in range(i+1, M):
#                 if lstM[j] == lstM[i]:
#                     arr[j] = arr[i]
#             lstN = lstN[:s+1] + lstN[e:]
#             break
#         elif lstM[i] > lstN[m]:
#             s = m + 1
#         elif lstM[i] < lstN[m]:
#             e = m - 1
#
# print(*arr)