# 2차원 리스트로 접근
# 체크 모양으로 맨 왼쪽위가 흰색인 케이스와 검정색인 케이스로 나눠
# 케이스와 색이 다른 숫자를 산출해냄

n, m = map(int, input().split())

arr = [list(map(str, input())) for _ in range(n)]
cnt = 64

for a in range(n-7):
    for b in range(m-7):
        temp1 = temp2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        temp1 += 1
                    if arr[i][j] != 'B':
                        temp2 += 1
                else:
                    if arr[i][j] != 'B':
                        temp1 += 1
                    if arr[i][j] != 'W':
                        temp2 += 1

        if temp1 < cnt:
            cnt = temp1
        if temp2 < cnt:
            cnt = temp2

print(cnt)

