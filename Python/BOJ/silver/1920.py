def bin(x):
    s = 0
    e = len(A) - 1
    while s <= e:
        m = (s+e)//2
        if A[m] == x:
            return 1
        elif A[m] > x:
            e = m - 1
        else:
            s = m + 1
    return 0

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()


for i in B:
    print(bin(i))