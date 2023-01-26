import sys
sys.stdin = open('PROBLEM3.txt')

N = int(input())
D = [input() for _ in range(4)]
L = [input() for _ in range(N)]

for i in range(len(L)): # 어떤 단어인지?
    visited = [0] * 4
    cnt = 0
    for j in range(len(L[i])): # 그 단어에서 글자를 순회
        for k in range(len(D)): # 주사위를 순회
            for l in range(len(D[k])): # 주사위 내부의 글자를 순회
                if L[i][j] == D[k][l] and not visited[k]: # 주사위 내부의 글자와 단어의 글자가 같고, 방문이 안찍혀있으면
                    visited[k] = 1                        # 방문찍고 cnt 올리고 break
                    cnt += 1
                    break
                elif visited[k]: # 주사위 방문이 이미 찍혀있으면 그냥 break로 다음 주사위 봄
                    break
            if cnt == len(L[i]): # 주사위 방
                break
        if cnt == len(L[i]):
            break
    if cnt == len(L[i]):
        print('YES')
    else:
        print('NO')
##################################
# import sys
# sys.stdin = open('PROBLEM3.txt')
#
# N = int(input())
# D = [input() for _ in range(4)]
# L = [input() for _ in range(N)]
#
# for i in range(len(L)): # 어떤 단어인지?
#     visited = [0] * 4
#     cnt = 0
#     for j in range(len(L[i])): # 그 단어에서 글자를 순회
#         for k in range(len(D)): # 주사위를 순회
#             for l in range(len(D[k])): # 주사위 내부의 글자를 순회
#                 if L[i][j] == D[k][l] and not visited[k]: # 주사위 내부의 글자와 단어의 글자가 같고, 방문이 안찍혀있으면
#                     visited[k] = 1                        # 방문찍고 cnt 올리고 break
#                     cnt += 1
#                     break
#                 elif visited[k]: # 주사위 방문이 이미 찍혀있으면 그냥 break로 다음 주사위 봄
#                     break
#             if cnt == len(L[i]): # 주사위 방
#                 break
#         if cnt == len(L[i]):
#             break
#     if cnt == len(L[i]):
#         print('YES')
#     else:
#         print('NO')


###################################
# N = int(input())
# str1 = list(input())
# str2 = list(input())
# str3 = list(input())
# str4 = list(input())
#
# for i in range(N):
#     word = list(input())
#     cnt = 0
#     if len(word) == 4 :
#         if word[0] in str1:
#             cnt += 1
#             if word[1] in str2 :
#                 cnt += 1
#                 if word[2] in str3 :
#                     cnt += 1
#                     if word[3] in str4:
#                         cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#                     if word[3] in str3:
#                         cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#                 if word[2] in str2 :
#                     cnt += 1
#                     if word[3] in str4:
#                         cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#                     if word[3] in str2:
#                         cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#                 if word[2] in str2 :
#                     cnt += 1
#                     if word[3] in str3:
#                         cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#                     if word[3] in str2:
#                         cnt += 1
#         elif word[0] in str2:
#             cnt += 1
#             if word[1] in str1 :
#                 cnt += 1
#                 if word[2] in str3:
#                     cnt += 1
#                     if word[3] in str4:
#                         cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#                     if word[3] in str3:
#                         cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#                 if word[2] in str1 :
#                     cnt += 1
#                     if word[3] in str4:
#                         cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#                     if word[3] in str1:
#                         cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#                 if word[2] in str1 :
#                     cnt += 1
#                     if word[3] in str3:
#                         cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#                     if word[3] in str1:
#                         cnt += 1
#         elif word[0] in str3:
#             cnt += 1
#             if word[1] in str1 :
#                 cnt += 1
#                 if word[2] in str2:
#                     cnt += 1
#                     if word[3] in str4:
#                         cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#                     if word[3] in str2:
#                         cnt += 1
#             elif word[1] in str2:
#                 cnt += 1
#                 if word[2] in str1 :
#                     cnt += 1
#                     if word[3] in str4:
#                         cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#                     if word[3] in str1:
#                         cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#                 if word[2] in str1 :
#                     cnt += 1
#                     if word[3] in str2:
#                         cnt += 1
#                 elif word[2] in str2:
#                     cnt += 1
#                     if word[3] in str1:
#                         cnt += 1
#         elif word[0] in str4:
#             cnt += 1
#             if word[1] in str1 :
#                 cnt += 1
#                 if word[2] in str2:
#                     cnt += 1
#                     if word[3] in str3:
#                         cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#                     if word[3] in str2:
#                         cnt += 1
#             elif word[1] in str2:
#                 cnt += 1
#                 if word[2] in str1 :
#                     cnt += 1
#                     if word[3] in str3:
#                         cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#                     if word[3] in str1:
#                         cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#                 if word[2] in str1 :
#                     cnt += 1
#                     if word[3] in str2:
#                         cnt += 1
#                 elif word[2] in str2:
#                     cnt += 1
#                     if word[3] in str1:
#                         cnt += 1
#     elif len(word) == 3:
#         if word[0] in str1:
#             cnt += 1
#             if word[1] in str2:
#                 cnt += 1
#                 if word[2] in str3:
#                     cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#                 if word[2] in str2:
#                     cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#                 if word[2] in str2:
#                     cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#         elif word[0] in str2:
#             cnt += 1
#             if word[1] in str1:
#                 cnt += 1
#                 if word[2] in str3:
#                     cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#                 if word[2] in str1:
#                     cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#                 if word[2] in str1:
#                     cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#         elif word[0] in str3:
#             cnt += 1
#             if word[1] in str1:
#                 cnt += 1
#                 if word[2] in str2:
#                     cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#             elif word[1] in str2:
#                 cnt += 1
#                 if word[2] in str1:
#                     cnt += 1
#                 elif word[2] in str4:
#                     cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#                 if word[2] in str1:
#                     cnt += 1
#                 elif word[2] in str2:
#                     cnt += 1
#         elif word[0] in str4:
#             cnt += 1
#             if word[1] in str1:
#                 cnt += 1
#                 if word[2] in str2:
#                     cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#             elif word[1] in str2:
#                 cnt += 1
#                 if word[2] in str1:
#                     cnt += 1
#                 elif word[2] in str3:
#                     cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#                 if word[2] in str1:
#                     cnt += 1
#                 elif word[2] in str2:
#                     cnt += 1
#     elif len(word) == 2 :
#         if word[0] in str1:
#             cnt +=1
#             if word[1] in str2:
#                 cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#         elif word[0] in str2:
#             cnt +=1
#             if word[1] in str1:
#                 cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#         elif word[0] in str3:
#             cnt +=1
#             if word[1] in str1:
#                 cnt += 1
#             elif word[1] in str2:
#                 cnt += 1
#             elif word[1] in str4:
#                 cnt += 1
#         elif word[0] in str4:
#             cnt +=1
#             if word[1] in str1:
#                 cnt += 1
#             elif word[1] in str2:
#                 cnt += 1
#             elif word[1] in str3:
#                 cnt += 1
#     elif len(word) == 1:
#         if word[0] in str1:
#             cnt += 1
#         elif word[0] in str2:
#             cnt += 1
#         elif word[0] in str3:
#             cnt += 1
#         elif word[0] in str4:
#             cnt += 1
#
#     if cnt == len(word):
#         print('YES')
#     else :
#         print('NO')