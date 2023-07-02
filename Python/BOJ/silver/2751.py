# 뱅글뱅글 돌아서 풀었는데 나중에 해보니까 sys.stdin.readline() 랑 sort만 써도 풀리더라구요,,

import sys
N = int(input())
num = [int(sys.stdin.readline()) for _ in range(N)]
nm = 0
a, b = abs(min(num)), max(num)
nm = a if a > b else b
arr = [0] * (nm+1)

for i in num:
    if i < 0 and arr[-i]:
        arr[-i] = 3
    elif i < 0:
        arr[-i] = 2
    elif arr[i]:
        arr[i] = 3
    else:
        arr[i] = 1

for i in range(len(arr)-1, -1, -1):
    if arr[i] == 3:
        print(-i)
        arr[i] = 1
    elif arr[i] == 2:
        print(-i)
for i in range(len(arr)):
    if arr[i] == 1:
        print(i)
