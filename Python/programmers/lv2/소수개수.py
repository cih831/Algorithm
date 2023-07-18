n = 437674
k = 3
answer = 0
trans = 0
cnt = 1

def is_prime(x):
    from math import sqrt

    for i in range(2, int(sqrt(x)) + 1):
        if not x % i:
            return False
    return True

while n:
    trans += (n % k) * cnt
    n //= k
    cnt *= 10

tmp = 0
cnt = 0
for idx in range(len(str(trans))):
    now = (trans // (10 ** idx) % 10) * (10 ** cnt)
    tmp += now
    cnt += 1
    if not now or idx == len(str(trans)) - 1:
        if tmp > 1 and is_prime(tmp):
            answer += 1
        tmp = 0
        cnt = 0

print(answer)