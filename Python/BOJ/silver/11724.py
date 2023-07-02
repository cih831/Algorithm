import sys

N, M = map(int, sys.stdin.readline().split())
E = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(M)])
pn = [n for n in range(N + 1)]

for item in E:
    if pn[item[0]] < pn[item[1]]:
        p = pn[pn[item[1]]]
        pn[item[1]] = pn[item[0]]
        while p != pn[item[0]]:
            pn[p], p = pn[item[0]], pn[p]
    else:
        p = pn[pn[item[0]]]
        pn[item[0]] = pn[item[1]]
        while p != pn[item[1]]:
            pn[p], p = pn[item[1]], pn[p]


print(len(set(pn[1:])))