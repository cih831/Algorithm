def solution(numbers):
    answer = []
    for num in numbers:
        if not num % 2:
            answer.append(num + 1)
        else:
            for i in range(500000000000000):
                if not (num - ((2 ** i) - 1)) % (2 ** (i + 1)):
                    answer.append(num + 2 ** (i - 1))
                    break
    return answer

print(solution([
    2, 7
]))

# 1 - 4
# print([x-1 for x in range(1, 1000, 4)])
# print([x for x in range(0, 999, 4)])

# 3 - 8
# print([x-1 for x in range(3, 1000, 8)])
# print([x for x in range(2, 999, 8)])

"""
1-4
3-8
7-16
15-32
31-64

1
3
7
15
"""