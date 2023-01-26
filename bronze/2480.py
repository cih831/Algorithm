arr = list(map(int, input().split()))

for i in range(2):
    cnt = 0
    for j in range(i, 3):
        if i == j:
            cnt += 1
    if cnt == 3 or cnt == 2:
        break