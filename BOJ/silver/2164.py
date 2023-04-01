# # 시간초과
# N = int(input())
# card = [i for i in range(1, N+1)]
# while card[0] != card[-1]:
#     card = card[2:] + [card[1]]
# print(card[0])


from collections import deque
d = deque()
for i in range(int(input())):
    d.append(i+1)
while len(d) > 1:
    d.popleft()
    d.append(d.popleft())
print(d[0])