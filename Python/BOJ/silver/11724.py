import sys

input = sys.stdin.readline

N, M = map(int, input().split())
E = sorted([sorted(list(map(int, input().split()))) for _ in range(M)])
pn = [n for n in range(N + 1)]

for item in E:
    if pn[item[0]] < pn[item[1]]:
        pn[item[1]] = pn[item[0]]
    else:
        pn[item[0]] = pn[item[1]]

for item in E[::-1]:
    if pn[item[0]] < pn[item[1]]:
        pn[item[1]] = pn[item[0]]
    else:
        pn[item[0]] = pn[item[1]]

print(len(set(pn[1:])))
