def solution(n):
    answer = n + 1
    while answer.bit_count() != n.bit_count():
        answer += 1
    return answer

"""
! programmers는 python 3.10 이전 버전이라 bit_count() 함수가 없음 !

def solution(n):
    def bit_count(num):
        return bin(num).count("1")
    answer = n + 1
    while bit_count(answer) != bit_count(n):
        answer += 1
    return answer
"""

print(solution(78))