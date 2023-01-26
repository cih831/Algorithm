import sys
from collections import deque

T = int(input())
for tc in range(1, T+1):
    com = sys.stdin.readline().rstrip()
    N = int(sys.stdin.readline().rstrip())
    a = sys.stdin.readline().rstrip()
    if not N:
        if 'D' in com:
            print('error')
        else:
            print('[]')
        continue
    arr = deque(map(str, a[1:-1].split(',')))
    cnt = 0
    rev = 0
    for i in com:
        if i == 'R':
            rev += 1
        else:
            if not arr:
                print('error')
                cnt += 1
                break
            else:
                if not rev % 2:
                    arr.popleft()
                else:
                    arr.pop()
    if not cnt:
        if rev % 2:
            arr.reverse()
            print('[' + ','.join(arr) + ']')
        else:
            print('[' + ','.join(arr) + ']')