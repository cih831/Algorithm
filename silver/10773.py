N = int(input())
num = [int(input()) for _ in range(N)]
stack = []

for i in num:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))