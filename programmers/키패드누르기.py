def solution(numbers, hand):
    answer = ''
    l, m, r = (1, 4, 7, -1), (2, 5, 8, 0), (3, 6, 9, -2)
    lh, rh = -1, -2
    for num in numbers:
        if num in l:
            answer += 'L'
            lh = num
        elif num in r:
            answer += 'R'
            rh = num
        else:
            if lh in l: l_dist = abs(m.index(num) - l.index(lh)) + 1
            else: l_dist = abs(m.index(num) - m.index(lh))
            if rh in r: r_dist = abs(m.index(num) - r.index(rh)) + 1
            else: r_dist = abs(m.index(num) - m.index(rh))
            if l_dist < r_dist:
                answer += 'L'
                lh = num
            elif l_dist > r_dist:
                answer += 'R'
                rh = num
            else:
                if hand == 'left':
                    answer += 'L'
                    lh = num
                else:
                    answer += 'R'
                    rh = num
    return answer

print(solution(
    [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
    "right"
))