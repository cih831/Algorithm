T = int(input())
for tc in range(1, T+1):
    PS = input()
    stack = []
    for item in PS:
        if item == '(':
            stack.append(item)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')