def solution(s):
    answer = 0
    d = {'}': '{', ')': '(', ']': '['}

    if len(s) % 2: return 0

    for _ in range(len(s)):
        s = s[1:] + s[0]
        stack = []
        for item in s:
            if item in '([{':
                stack.append(item)
            else:
                if not stack: break
                tmp = stack.pop()
                if d[item] != tmp: break
        else:
            answer += 1

    return answer

print(solution(
    "}]()[{"
))