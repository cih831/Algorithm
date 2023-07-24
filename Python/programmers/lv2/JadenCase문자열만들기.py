def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i - 1] == ' ' or i == 0:
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer