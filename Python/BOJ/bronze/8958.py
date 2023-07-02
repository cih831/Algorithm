# 만약 O면, 이전 점수에 +1 하여 score 에 가산
# 첫자리는 1로 인덱스 에러 조심

T = int(input())

for tc in range(T):
    OX = input()
    arr = [0] * len(OX)
    score = 0

    for i in range(len(OX)):
        if OX[i] == 'O':
            arr[i] = 1
            if i != 0 and OX[i-1] == 'O':
                arr[i] = arr[i-1] + 1

    for i in arr:
        score += i

    print(score)