N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
cnt = my_sum = 0

for i in range(N-1, -1, -1):
    while my_sum + 100 * coin[i] <= K:
        my_sum += 100 * coin[i]
        cnt += 100
    while my_sum + 50 * coin[i] <= K:
        my_sum += 50 * coin[i]
        cnt += 50
    while my_sum + coin[i] <= K:
        my_sum += coin[i]
        cnt += 1

print(cnt)