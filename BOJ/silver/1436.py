# 665 부터 숫자를 세는 list 생성하여 666이 들어가는 숫자만 list에 저장
# len(list) == N 이면 반복문을 종료하고 list[-1] 출력

N = int(input())
s = [665]

while len(s) < N + 1:
    tmp = s[-1]
    while True:
        tmp += 1
        if '666' in str(tmp):
            break
    s += [tmp]

print(s[-1])