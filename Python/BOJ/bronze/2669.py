arr = [[0]*100 for _ in range(100)]

sqr = [list(map(int, input().split())) for _ in range(4)]
cnt = 0

for i in range(4):
    for j in range(sqr[i][0], sqr[i][2]):
        for k in range(sqr[i][1], sqr[i][3]):
            arr[j][k] += 1

for i in range(100):
    for j in range(100):
        if arr[i][j]:
            cnt += 1

print(cnt)