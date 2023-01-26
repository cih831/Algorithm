# A, B = map(int, input(),split())
# B//A = a * b (a,b는 자연수)
# list된 값들 중에 a와 b가 서로소인 값만 출력
# list에서 a+b가 가장 작은 값을 선택
# 출력 (a*A, b*A)

# A, B = map(int, input().split())
# X = B//A
# lst = [[1, X]]
# for i in range(1, X):
#     if i * i > X:
#         break
#     if X % i == 0:
#         a, b = i, X//i
#         while b % a != 0:
#             a, b = b, a % b
#             if b == 1:
#                 lst += [[i, X//i]]
# ms = sum(lst[0])
# my_lst = []
# for i in lst:
#     if ms > sum(i):
#         ms = sum(i)
#         my_lst = i
#
# print(my_lst[0]*A, my_lst[1]*A)

#
#
# N, M = map(int, input().split())
# constant = M//N
# div_num = constant
# for i in range(1, div_num+1):
#     if i * i > div_num:
#         break
#     if div_num % i == 0:
#         x = i
#         y = constant//i
#         while x % y != 0:
#             x, y = y, x % y
#         if y == 1:
#             a = i
#             b = constant//i
# print(a*N, b*N)

A, B = map(int, input().split())
X = B//A
lst = [[1, X]]
for i in range(1, X+1):
    if i * i > X:
        break
    if X % i == 0:
        a, b = i, X//i
        while a % b != 0:
            a, b = b, a % b
            if b == 1:
                a = i
                b = X//i
print(a*A, b*A)