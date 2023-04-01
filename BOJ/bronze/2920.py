s = list(map(int, input().split()))

cnt = 0

if s[1] == s[0] + 1:
    for i in range(len(s)-1):
        if s[i+1] == s[i] + 1:
            cnt += 1
elif s[1] == s[0] - 1:
    for i in range(len(s)-1):
        if s[i+1] == s[i] - 1:
            cnt -= 1

if cnt == 7:
    print('ascending')
elif cnt == -7:
    print('descending')
else:
    print('mixed')