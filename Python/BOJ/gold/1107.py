N = int(input())
ans = abs(100 - N)
M = int(input())
if M:
    broken = list(input().split())
else:
    broken = []

for num in range(1000001):
    for N in str(num):
        if N in broken:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - N))

print(ans)