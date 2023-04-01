arr = [1, 2, 4]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    while len(arr) < N:
        arr.append(arr[-1] + arr[-2] + arr[-3])
    print(arr[N-1])