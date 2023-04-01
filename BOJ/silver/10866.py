import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    d = sys.stdin.readline().split()
    if d[0] == 'push_front':
        stack = [d[1]] + stack
    elif d[0] == 'push_back':
        stack.append(d[1])
    elif d[0] == 'pop_front':
        if stack:
            print(stack[0])
            stack = stack[1:]
        else:
            print(-1)
    elif d[0] == 'pop_back':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif d[0] == 'size':
        print(len(stack))
    elif d[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif d[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)