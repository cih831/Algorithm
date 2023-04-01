import sys

N = int(input())
conf = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
conf.sort(key=lambda x: (x[1], x[0]))
cnt = 0
stack = [conf[0]]
for i in range(1, N):
    if conf[i][0] >= stack[-1][1]:
        stack.append(conf[i])
print(len(stack))