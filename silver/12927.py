L = [0] + list(input())
cnt = 0

while 'Y' in L and cnt < len(L):
    for i in range(len(L)):
        if L[i] == 'Y':
            cnt += 1
            for j in range(i, len(L), i):
                L[j] = 'N' if L[j] == 'Y'else 'Y'

if cnt == len(L):
    cnt = -1

print(cnt)