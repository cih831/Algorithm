while 1:
    S = input()
    stack = []
    if S == '.':
        break
    for i in S:
        if i in '([':
            stack.append(i)
        elif i == ')' and stack:
            a = stack.pop()
            if a == '[':
                print('no')
                break
        elif i == ']' and stack:
            a = stack.pop()
            if a == '(':
                print('no')
                break
        elif i in '])' and not stack:
            print('no')
            break
    else:
        if stack:
            print('no')
        else:
            print('yes')