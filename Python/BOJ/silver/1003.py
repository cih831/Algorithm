import sys

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    if cnt[n] != 0:
        return cnt[n]
    cnt[n] = fibo(n-1) + fibo(n-2)
    return cnt[n]

T = int(sys.stdin.readline())
cnt = [0] * 41

for _ in range(T):
    N = int(sys.stdin.readline())
    fibo(N)
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(fibo(N-1), fibo(N))