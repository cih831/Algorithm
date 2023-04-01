N = int(input())
lst = [N]
my_lst = [] # 최대 리스트를 저장할 공간
l = 0 # 최대 리스트 길이
for i in range(N, N//2, -1): # 두 번째 값 범위
    lst += [i]
    while lst[-1] >= 0: # 음수가 나올 때까지 돌림
        lst += [lst[-2]-lst[-1]] # 마지막 전에서 마지막 값을 빼서 lst에 추가
    lst.pop() # 음수 값 제거
    if len(lst) > l: # lst 길이가 최대 길이보다 길면 리스트와 길이를 저장
        l = len(lst)
        my_lst = lst
    lst = lst[:1] # N 까지만 남기고 전부 제거해서 lst 를 초기 상태로 되돌려줌(2번째 값이 정상적으로 들어갈 수 있도록)

print(l)
print(*my_lst)