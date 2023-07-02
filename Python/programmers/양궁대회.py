import itertools

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]
answer = []

score = 0
for i in range(11):                                          # 어피치 점수 계산
    if info[i]:
        score += 10 - i

max_diff = 0
point = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
combi = []
p_tmp = [11]
for i in range(10, 0, -1):                                   # 모든 경우의 수,,ㅠㅠ
    combi.extend(list(itertools.combinations(point, i)))

for item in combi:
    item = list(item)
    ans = [0] * 11
    apeach = 0

    for p in item:
        ans[10 - p] = info[10 - p] + 1

    if n < sum(ans):                                         # 화살 개수가 초과되면 가지치기
        continue

    for i in range(10):
        if ans[i] and info[i]:
            apeach += 10 - i

    diff = sum(item) - (score - apeach)

    if sum(item) <= score - apeach or diff < max_diff:   # 어피치 보다 낮은 점수, 최고 점수 편차보다 작으면 가지치기
        continue

    if n - sum(ans) > 0:
        ans[10] += sum(info) - sum(ans)
        item.append(0)

    item.sort()
    if diff == max_diff:
        flag = 0
        for i in range(min(len(p_tmp), len(item))):
            if p_tmp[i] < item[i] or (p_tmp[i] == item[i] and answer[i] < item[i]):
                flag = 1
                break
        if flag:
            continue

    max_diff = diff
    answer = ans
    p_tmp = item

print(answer if answer else [-1])
