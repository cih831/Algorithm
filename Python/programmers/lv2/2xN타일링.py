def solution(n):
    # if n == 1: return 1

    # dp = [0] * n
    # dp[0], dp[1] = 1, 2
    # for i in range(2, n):
    #     dp[i] = dp[i - 1] + dp[i - 2]

    x, y = 1, 1
    for i in range(n): x, y = x + y, x
    
    return y % 1000000007

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(60000))

"""
1
2
3
5
8
13
21
34
55
"""