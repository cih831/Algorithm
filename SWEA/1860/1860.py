import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    stack = []

    for i in range(P[-1]+1):
        if i != 0 and i % M == 0:
            stack += [1]*K
        if i in P:
            if stack:
                stack.pop()
            else:
                A = 'Impossible'
                break
    else:
        A = 'Possible'

    print(f'#{tc} {A}')