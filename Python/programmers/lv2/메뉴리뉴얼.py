from itertools import combinations

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
answer = []

d = {}

for menus in orders:
    for num in course:
        if not num in d:
            d[num] = {}
        tmp = list(combinations(sorted(menus), num))
        for t in tmp:
            t = ''.join(t)
            if t in d[num]:
                d[num][t] += 1
            else:
                d[num][t] = 1

for num in course:
    tmp = 2
    res = []
    for key, value in d[num].items():
        if value > tmp:
            tmp = value
            res = [key]
        elif value == tmp:
            res.append(key)
    answer.extend(res)

answer.sort()
print(answer)