S = input()

alphas = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(alphas)):
    for j in range(len(S)):
        if alphas[i] == S[j]:
            print(j, end = ' ')
            break
    else:
        print(-1, end = ' ')