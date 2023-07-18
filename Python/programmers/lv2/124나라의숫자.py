def solution(n):
    answer = ''
    while n:
        answer = '412'[n % 3] + answer
        n = n // 3 if n % 3 else n // 3 - 1
    return answer

print(1, solution(1))
print(2, solution(2))
print(3, solution(3))
print(4, solution(4))
print(5, solution(5))
print(6, solution(6))
print(7, solution(7))
print(8, solution(8))
print(9, solution(9))
print(10, solution(10))
print(11, solution(11))
print(12, solution(12))
print(13, solution(13))
print(33, solution(30))

"""
1 1
2 2
3 4
4 11
5 12
6 14
7 21
8 22
9 24
10 41
11 42
12 44
13 111
14 112
15 114
16 121
17 122
18 124
19 141
20 142
21 144
22 211
23 212
24 214
25 221
26 222
27 224
28 241
29 242
30 244
"""