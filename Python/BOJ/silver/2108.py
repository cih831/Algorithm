from collections import Counter
import sys

N = int(input())
num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()
a = b = c = d = 0
a = (sum(num)/N)
b = num[N//2]
d = num[-1] - num[0]

cnt = Counter(num).most_common(2)
if len(num) != 1 and cnt[0][1] == cnt[1][1]:
    c = cnt[1][0]
else:
    c = cnt[0][0]

print(int(round(a)))
print(b)
print(c)
print(d)