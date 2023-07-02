import sys
input = sys.stdin.readline

def recur(idx, hp_now=100, happy_now=0):
    global ans
    ans = max(ans, happy_now)
    for j in range(idx + 1, N):
        if hp_now - hp[j] > 0:
            recur(j, hp_now - hp[j], happy_now + happy[j])


N = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))
ans = 0

for i in range(N):
    if hp[i] < 100:
        recur(i, 100 - hp[i], happy[i])

print(ans)