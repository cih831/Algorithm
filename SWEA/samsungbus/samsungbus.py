import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    PP = [int(input()) for _ in range(P)]
    cnt_bus = [0] * P

    for i in range(N):
        for j in range(P):
            if arr[i][0] <= PP[j] <= arr[i][1]:
                cnt_bus[j] += 1

    print(f'#{tc}', *cnt_bus)