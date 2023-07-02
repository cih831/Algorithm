T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [0]*N
    arr[M] = '!'
    cnt = 0

    while '!' in arr:
        if lst[0] != max(lst):
            lst.append(lst.pop(0))
            arr.append(arr.pop(0))
        else:
            if arr[0] == '!':
                arr.pop(0)
                lst.pop(0)
                cnt += 1
                print(cnt)
            else:
                arr.pop(0)
                lst.pop(0)
                cnt += 1