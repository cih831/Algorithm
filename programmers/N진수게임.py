def solution(n, t, m, p):
    answer = ''

    tmp = '0' # 전체 정답 저장
    num = 0 # 현재 숫자

    while len(tmp) < t * m: # 마지막 바퀴 길이까지 계산
        num += 1
        num_tmp = num
        chg = ''
        while num_tmp: # 아스키 코드 통해서 n진수 변환
            chg_tmp = num_tmp % n
            chg = str(chg_tmp) + chg if chg_tmp < 10 else chr(55 + chg_tmp) + chg
            num_tmp //= n
        tmp += chg

    while len(answer) < t: # 튜브의 정답 나열
        answer += tmp[p - 1]
        p += m

    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))