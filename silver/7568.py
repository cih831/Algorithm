N = int(input())
big = [list(map(int, input().split())) for _ in range(N)]
rank = [1]*N

for i in range(N):
    for j in range(N):
        if big[i][0] < big[j][0] and big[i][1] < big[j][1]:
            rank[i] += 1

print(*rank)