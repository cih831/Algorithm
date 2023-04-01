T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(str, input().split())) for _ in range(N)]
    cloth = {}
    for item in lst:
        if item[1] in cloth:
            cloth[item[1]] += 1
        else:
            cloth[item[1]] = 2

    ans = 1
    for key in cloth:
        ans *= cloth[key]

    print(ans-1)





# 시간초과
# from collections import deque
#
# def recur(n=0, cnt=0, cloth=deque()):
#     global ans
#     if n == N:
#         if cnt:
#             ans += 1
#         return
#     if not lst[n][1] in cloth:
#         cloth.append(lst[n][1])
#         recur(n+1, cnt+1, cloth)
#         cloth.pop()
#     recur(n+1, cnt, cloth)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = [list(map(str, input().split())) for _ in range(N)]
#     ans = 0
#
#     recur()
#
#     print(ans)