N = int(input())
L = ['!'] + list(map(int, input().split()))
S = int(input())
num = [list(map(int, input().split())) for _ in range(S)]

for i in range(len(num)): # 카드표 순회
    if num[i][0] == 1: # 남자면
        for j in range(num[i][1], len(L), num[i][1]): # 카드 숫자 배수들을 반전
            L[j] = 1 if L[j] == 0 else 0
    else: # 여자면
        for j in range(len(L)//2): # 양옆을 확인하여
            if num[i][1] + j <= N and num[i][1] - j >= 1 and L[num[i][1]+j] == L[num[i][1]-j]: # 전구 상태가 같으면 계속 진행
                if j == 0:
                    L[num[i][1]] = 1 if L[num[i][1]] == 0 else 0
                else:
                    L[num[i][1]+j] = 1 if L[num[i][1]+j] == 0 else 0
                    L[num[i][1]-j] = 1 if L[num[i][1]-j] == 0 else 0
            else: # 다르면 멈춤
                break

L = L[1:]
for i in range(0, 81, 20):
    print(*L[i:i+20])
