def solution(n):
    if n <= 2:
        return n
    arr = [0] * (n + 1)
    arr[1], arr[2] = 1, 2
    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]%1234567

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))

# def jumpCase(num):
#     if num == 1:
#         return 1
#     a, b = 1, 2
#     for i in range(2,num):
#         a, b = b, a+b
#     return b

# #아래는 테스트로 출력해 보기 위한 코드입니다.
# print(jumpCase(1))
# print(jumpCase(2))
# print(jumpCase(4))
