# s e 를 0으로 초기 설정
# s 부터 e 까지 더한 값이 M보다 작으면 s를 한칸 밀고
# M보다 크면 e를 한칸 밀어줌
# 같으면 cnt += 1

n, m = map(int, input().split())
li = list(map(int, input().split()))
cnt = s = e = 0
tmp = li[0]

while e < n:
    try:
        if tmp == m:
            cnt += 1
            e += 1
            tmp += li[e]
        elif tmp < m:
            e += 1
            tmp += li[e]
        else:
            tmp -= li[s]
            s += 1
    except:
        break

print(cnt)