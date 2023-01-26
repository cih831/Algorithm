from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt = [0]*25*25
num = 2

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            q = deque()
            q.append([i, j])
            arr[i][j] = num
            cnt[num] += 1
            while q:
                x, y = q.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1:
                        q.append([nx, ny])
                        arr[nx][ny] = num
                        cnt[num] += 1
            num += 1

cnt = sorted(cnt[2:num])
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])