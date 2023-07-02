# N = int(input())
# a = N - len(str(N)) * 9 # 생성자의 모든 숫자가 9일 경우가 고려할 수 있는 최소이기 때문에
# my_min = 0
# for i in range(a, N):
#     b = i # 결과값 저장
#     c = i # 한자리 씩 빼줄 곳
#     while c:
#         b += c % 10
#         c = c // 10
#     if b == N: # 작은 숫자부터 찾아가기 때문에 값을 찾으면 바로 break
#         my_min = i
#         break
# print(my_min)

N = int(input())
start = max(0, N - len(str(N)) * 9)
end = max(0, N - len(str(N)))

answer = 0
for i in range(start, end):
    if sum([int(number) for number in str(i)]) + i == N:
        answer = i
        break
print(answer)