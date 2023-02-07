import sys
input = sys.stdin.readline
num = 1000000007

def recur(b, t):
    if t == 1:
        return b % num
    if t % 2 == 0:
        temp = recur(b, t // 2)
        return (temp * temp) % num
    else:
        return b * recur(b, t - 1) % num

M = int(input())
ans = 0
for _ in range(M):
    N, S = map(int, input().split())
    ans += S * recur(N, num - 2) % num
    ans %= num

print(ans)