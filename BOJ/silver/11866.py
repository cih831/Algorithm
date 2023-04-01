N, K = map(int, input().split())
num = []
num += [i for i in range(1, N+1)]
point = -1

print('<', end='')
while num:
    for i in range(K):
        point += 1
        if point == len(num):
            point = 0
    if not len(num) == 1:
        print(num.pop(point), end=', ')
    else:
        print(num.pop(point), end='')
    point -= 1
print('>')