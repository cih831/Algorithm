import sys

N = int(sys.stdin.readline())
P = []
for _ in range(N):
    x, y = sys.stdin.readline().split()
    P += [[int(x), y]]

P.sort(key=lambda x:x[0])

for i in P:
    print(*i)