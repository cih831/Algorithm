def solution(s):
    answer = [0, 0]
    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        s = bin(s.count('1'))[2:]
    return answer

# def solution(s):
#     if s == 1: return [0, 0]

#     answer = [1, 0]
#     answer[1] += s.count('0')
#     now = s.count('1')
#     cnt = 0
#     while now != 1:
#         tmp = now
#         while tmp != 1:
#             if tmp % 2: cnt += 1
#             else: answer[1] += 1
#             tmp //= 2
#         cnt += 1
#         now, cnt = cnt, 0
#         answer[0] += 1

#     return answer

print(solution(
    "1111111"
))