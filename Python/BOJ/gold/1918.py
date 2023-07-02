formula = list(input())
stack = []
postfix = ''

for i in formula:
    if i == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    elif i == '(':
        stack.append(i)
    elif i in '*/':
        while stack and stack[-1] in '*/':
            postfix += stack.pop()
        stack.append(i)
    elif i in '+-':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.append(i)
    else:
        postfix += i
    # print(stack, formula, postfix)

while stack:
    postfix += stack.pop()

print(postfix)