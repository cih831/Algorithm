import sys
from collections import deque
input = sys.stdin.readline

front = list(input().rstrip())
back = deque()
M = int(input())

for _ in range(M):
    command = input().split()
    if command[0] == 'P':
        front.append(command[1])
    elif command[0] == 'B' and front:
        front.pop()
    elif command[0] == 'L' and front:
        back.appendleft(front.pop())
    elif command[0] == 'D' and back:
        front.append(back.popleft())

front += back

print(''.join(front))