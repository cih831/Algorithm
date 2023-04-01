N, M = map(int, input().split())
pok = ['']
pok_dic = {}
for i in range(N):
    tmp = input()
    pok.append(tmp)
    pok_dic[tmp] = i + 1
for _ in range(M):
    tmp = input()
    if tmp.isdecimal():
        print(pok[int(tmp)])
    else:
        print(pok_dic[tmp])