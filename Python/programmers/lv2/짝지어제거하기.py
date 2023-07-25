def solution(s):
    stack = []
    for item in s:
        if stack and stack[-1] == item:
            stack.pop()
        else:
            stack.append(item)
    return 0 if stack else 1

print(solution('baabaa'))