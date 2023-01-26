def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n = int(input())

ans = 0
row = [0] * n

n_queens(0)
print(ans)


"""
===========
  시간초과
===========

def N_Queen(x = 0, arr = [], Q = ()):
    global cnt

    tmp = []
    if Q:
        tmp.append(Q)
        for i in range(8):
            nx, ny = Q
            nx += dx[i]
            ny += dy[i]
            while 0 <= nx < N and 0 <= ny < N:
                tmp.append((nx, ny))
                nx += dx[i]
                ny += dy[i]

    for y in range(N):
        if not (x, y) in arr + tmp:
            if x == N - 1:
                cnt += 1
            else:
                N_Queen(x + 1, arr + tmp, (x, y))


N = int(input())
dx, dy = (1, 0, -1, 0, -1, -1, 1, 1), (0, 1, 0, -1, -1, 1, -1, 1)
cnt = 0
N_Queen()

print(cnt)
"""