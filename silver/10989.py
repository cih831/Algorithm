import sys
N = int(sys.stdin.readline())
num = [0]*10001

for _ in range(N):
    num[int(sys.stdin.readline())] += 1

for i in range(10001):
    while num[i]:
        print(i)
        num[i] -= 1