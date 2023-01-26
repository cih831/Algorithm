N, M = map(int, input().split())
d = {}

for _ in range(N):
    site, password = input().split()
    d[site] = password

for _ in range(M):
    print(d[input()])