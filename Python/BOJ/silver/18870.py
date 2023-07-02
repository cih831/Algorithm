N = int(input())
arr = list(map(int, input().split()))
arr_set = sorted(list(set(arr)))

d = {arr_set[i]: i for i in range(len(arr_set))}

for item in arr:
    print(d[item], end=' ')