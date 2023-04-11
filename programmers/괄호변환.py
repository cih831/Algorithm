def solution(p):
    answer = ''
    stack, flag = [], False
    u = v = ''
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack.append('(')
            cnt += 1
        else:
            if stack:
                stack.pop()
            else:
                flag = True
            cnt -= 1
        if not cnt:
            if i < len(p) - 1:
                v = solution(p[i + 1:])
            if flag:
                tmp = ''
                for j in range(len(p[1:i])):
                    if p[1 + j] == '(':
                        tmp += ')'
                    else:
                        tmp += '('
                u = '(' + v + ')' + tmp
            else:
                u = p[:i + 1] + v
            break

    answer = u
    return answer

print(solution("()))((()"))