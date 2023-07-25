def solution(n):
    answer = 1
    if n > 2:
        s, e = 1, 2
        tmp = 1
        while e <= n // 2 + 2:
            if tmp < n:
                tmp += e
                e += 1
            elif tmp > n:
                tmp -= s
                s += 1
            else:
                answer += 1
                tmp += e
                e += 1
    return answer

print(solution(5))