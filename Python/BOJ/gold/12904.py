import sys
input = sys.stdin.readline
S, T = input().rstrip(), input().rstrip()
S_, S_len, s, e, flag = S[::-1], len(S), 0, len(T) - 1, 1
ans = 0

while 0 <= s <= e and e - s >= S_len - 1:
    if (flag and T[s:e + 1] == S) or (not flag and T[s:e + 1] == S_):
        ans = 1
        break

    if flag:
        if T[e] == 'B':
            flag = 0
        e -= 1  
    else:
        if T[s] == 'B':
            flag = 1
        s += 1

print(ans)

# import sys
# from collections import deque
# input = sys.stdin.readline

# S, T = input().rstrip(), input().rstrip()
# q = deque()
# q.append(S)
# while q:
#     word = q.popleft()
#     wordA = word + 'A'
#     Bword = word[::-1] + 'B'
#     if T in (wordA, Bword):
#         print(1)
#         break

#     if wordA in T or wordA[::-1] in T: q.append(wordA)
#     if Bword in T or Bword[::-1] in T: q.append(Bword)

# else:
#     print(0)