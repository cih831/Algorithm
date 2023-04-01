string = input()
bomb = input()
check = bomb[-1]
l = len(bomb)

stack = []

for char in string:
    stack.append(char)
    if char == check and ''.join(stack[-l:]) == bomb:
        del stack[-l:]

print(''.join(stack) if stack else 'FRULA')
        

"""
==============
재귀 시간초과
==============

import sys
sys.setrecursionlimit(1000000)

def recur(s, b, idx = 0):
    while idx < len(s) - len(b):
        if s[idx] == b[0]:
            s = recur(s, b, idx + 1)
            for i in range(len(b)):
                if s[idx + i] != b[i]:
                    break
            else:
                s = s[:idx] + s[idx + i + 1:]
                continue
        idx += 1
    return s if s else 'FRULA'

string = input()
bomb = input()

print(recur(string, bomb))
"""