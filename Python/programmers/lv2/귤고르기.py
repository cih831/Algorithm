def solution(k, tangerine):
    answer = 0
    lst = [0] * (max(tangerine) + 1)
    for tan in tangerine:
        lst[tan] += 1
    lst.sort(reverse=True)
    cnt = 0
    for i in range(len(lst)):
        cnt += lst[i]
        if cnt >= k:
            return i + 1

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))