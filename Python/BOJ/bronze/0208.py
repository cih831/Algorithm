# n = int(input())

# for i in range(n):
#     print(' '*(n-i-1)+'*'*(i+1))

# num = list(map(int, input().split()))
# total = 0

# for i in num:
#     total += i**2

# print(total % 10)

# print('Hello World!')


# max_num = 0
# cnt = 0

# for i in range(9):
#     temp = int(input())
#     if temp > max_num:
#         max_num = temp
#         cnt = i + 1

# print(max_num)
# print(cnt)

# t = 1
# for i in range(3):
#     temp = int(input())
#     t *= temp

# a = str(t)

# for i in range(10):
#     print(a.count(str(i)))


# for i in range(100):
#     try:
#         R , S = input().split()
#         P = ''
        
#         for i in S:
#             P += f'{i * int(R)}'
#         print(P)

#     except:
#         continue

# N = int(input())

# for i in range(1, 10):
#     print(f'{N} * {i} = {i * N}')

# N = int(input())

# for i in range(N):
#     print(i + 1)

N = int(input())

for i in range(N):
    print(N - i)