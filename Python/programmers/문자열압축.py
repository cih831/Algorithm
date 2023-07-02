def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        tmp = ''
        idx = 0
        while idx < len(s):
            cnt = 1
            char = s[idx:idx + i]
            # while s[idx:idx + cnt * i] == s[idx + i:idx + (cnt + 1) * i]:
            while s[idx + (cnt - 1) * i:idx + cnt * i] == s[idx + cnt * i:idx + (cnt + 1) * i]:
                cnt += 1
            if cnt > 1:
                tmp += str(cnt) + char
                idx += cnt * i
            else:
                tmp += char
                idx += i
        answer = min(answer, len(tmp))
    return answer

ip = "aaaabbaccc"
# ip = "ababcdcdababcdcd"
# ip = "abcabcdede"
# ip = "abcabcabcabcdededededede"
# ip = "xababcdcdababcdcd"
print(solution(ip))