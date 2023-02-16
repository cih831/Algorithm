def rank():
    global home, chicken
    for h in range(len(home)):
        for c in range(len(chicken)):
            d = abs(home[h][0] - chicken[c][0]) + abs(home[h][1] - chicken[c][1])
            if d < home[h][2]:
                home[h][2] = d
                tmp = c
        chicken[tmp][2] += 1

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
home = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j, 0])
        elif arr[i][j] == 1:
            home.append([i, j, 10000000])

rank()
chicken.sort(key=lambda x: -x[2])
chicken = chicken[:M]
for h in home:
    h[2] = 10000000
rank()

my_sum = 0
for h in home:
    my_sum += h[2]
print(my_sum)