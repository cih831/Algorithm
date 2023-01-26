arr = [[0]*1001 for _ in range(1001)]

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0]*(n+1)

for i in range(n):
    for j in range(paper[i][0], paper[i][0]+paper[i][2]):
        arr[j][paper[i][1]:paper[i][1]+paper[i][3]] = [i + 1]*paper[i][3]


for i in range(1001):
    for j in range(1001):
        cnt[arr[i][j]] += 1

for i in range(1, n+1):
    print(cnt[i])