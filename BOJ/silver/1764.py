import sys
N, M = map(int, sys.stdin.readline().split())
lst = [sys.stdin.readline() for _ in range(N)]
lst2 = [sys.stdin.readline() for _ in range(M)]

nn = list(set(lst) & set(lst2))
print(len(nn))
for name in sorted(nn):
    print(name, end='')