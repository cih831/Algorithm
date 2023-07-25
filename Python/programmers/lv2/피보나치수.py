def solution(n):
    x, y, cnt = 1, 1, 2
    while cnt < n:
        x, y, cnt = x + y, x, cnt + 1
    return x % 1234567

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