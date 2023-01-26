import sys
N, M = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
s, e = 1, max(T)

while s <= e:
    m = (s+e) // 2
    cnt = 0
    for i in T:
        if i > m:
            cnt += i - m # 나무 길이에서 중간값을 뺀게 양수면 더해줌
    if cnt >= M: # 필요한 나무보다 많이 잘랐으면
        s = m + 1 # 시작점을 높여서 덜 자르게 함
    else: # 필요한 나무보다 덜 잘랐으면
        e = m - 1 # 마지막 지점을 낮춰서 더 자르게 함

print(e)