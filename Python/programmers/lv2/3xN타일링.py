# def solution(n):
#     dp = [0] * (n + 1)
#     dp[2], dp[4] = 3, 11
#     for i in range(4, n + 1, 2):
#         dp[i] = dp[i - 2] * 3 + sum(dp[:i - 2]) * 2 + 2
#     print(dp)
#     return dp[n]

def solution(n):
    x, y = 11, 3
    for i in range(n//2 - 2):
        x, y = x * 3 + y * 2 + 2, x + y
    return x % 1000000007 if n != 2 else 3

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))