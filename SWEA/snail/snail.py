import sys
sys.stdin = open('input.txt')

# N*N arr
# 벽을 만나거나 다음 갈 곳이 True 면 꺽기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    p = [0, 0]
    num = 1

    while num < N * N:
        while p[1] + 1 < N and arr[p[0]][p[1]+1] == 0:
            arr[p[0]][p[1]] = num
            p[1] += 1
            num += 1
        while p[0] + 1 < N and arr[p[0]+1][p[1]] == 0:
            arr[p[0]][p[1]] = num
            p[0] += 1
            num += 1
        while p[1] - 1 > -1 and arr[p[0]][p[1]-1] == 0:
            arr[p[0]][p[1]] = num
            p[1] -= 1
            num += 1
        while arr[p[0]-1][p[1]] == 0:
            arr[p[0]][p[1]] = num
            p[0] -= 1
            num += 1
    arr[p[0]][p[1]] = num

    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])