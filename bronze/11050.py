N, K = map(int, input().split())
x = y = 1
for i in range(1, N+1):
    x *= i
for i in range(1, K+1):
    y *= i
for i in range(1, N-K+1):
    y *= i

print(x//y)