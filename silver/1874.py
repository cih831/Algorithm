# 1 ~ n 까지의 list 생성
# push pop 하며 출력
n = int(input())
num = [int(input()) for _ in range(n)]
lst = [i for i in range(n, 0, -1)]
tmp = []
result = []
while lst:
    tmp += [lst.pop()]
    result += ['+']
    while tmp and num[0] == tmp[-1]:
        result += ['-']
        tmp.pop()
        num.pop(0)
if tmp:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])