N = int(input())
arr = sorted(list(map(int, input().split())))
arr_sum = [arr[0]]

for i in range(1, N):
    arr_sum.append(arr[i] + arr_sum[i-1])

print(sum(arr_sum))