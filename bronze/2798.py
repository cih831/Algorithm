N, M = map(int, input().split())
C = list(map(int, input().split()))
C.sort()
c = len(C)
mm = 0

for i in  range(c-2):
    for j in range(i+1, c-1):
        for k in range(j+1, c):
            if C[i] + C[j] + C[k] > M:
                break
            elif C[i] + C[j] + C[k] > mm:
                mm = C[i] + C[j] + C[k]

print(mm)