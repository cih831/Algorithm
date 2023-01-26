import sys
M = int(input())
S = set()
for _ in range(M):
    command = sys.stdin.readline().strip().split()
    if len(command) == 1:
        c = command[0]
    else:
        c, x = command[0], command[1]
        x = int(x)
    if c == 'add':
        S.add(x)
    elif c == 'remove':
        S.discard(x)
    elif c == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif c == 'all':
        S = set([i for i in range(1, 21)])
    else:
        S = set()