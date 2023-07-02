while 1:
    T = list(map(int, input().split()))
    if not T[0]:
        break
    T.sort()
    if T[-1]**2 == T[0]**2 + T[1]**2:
        print('right')
    else:
        print('wrong')