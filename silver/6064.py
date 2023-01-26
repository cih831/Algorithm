T = int(input())
for tc in range(1, T+1):
    M, N, x, y = map(int, input().split())
    M_lst = [x]
    N_lst = [y]
    if M > N:
        a, b = M, N
    else:
        a, b = N, M
    while a % b != 0:
        a, b = b, a % b
    LCM = N * M // b
    while M_lst[-1] - x != LCM:
        M_lst.append(M_lst[-1]+M)
    while N_lst[-1] - y != LCM:
        N_lst.append(N_lst[-1]+N)

    i = j = 0
    ans = -1
    while M_lst[i] != N_lst[j]:
        if M_lst[i] > N_lst[j]:
            j += 1
        else:
            i += 1
        if i == len(M_lst) or j == len(N_lst):
            break
    else:
        ans = M_lst[i]
    print(ans)
