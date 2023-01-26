import sys
input = sys.stdin.readline

N = int(input())
a1, a2, a3 = map(int, input().split())
max_arr = [a1, a2, a3]
min_arr = [a1, a2, a3]
for _ in range(N - 1):
    arr = list(map(int, input().split()))
    mx1 = arr[0] + max(max_arr[0], max_arr[1])
    mx2 = arr[1] + max(max_arr[0], max_arr[1], max_arr[2])
    mx3 = arr[2] + max(max_arr[1], max_arr[2])
    mn1 = arr[0] + min(min_arr[0], min_arr[1])
    mn2 = arr[1] + min(min_arr[0], min_arr[1], min_arr[2])
    mn3 = arr[2] + min(min_arr[1], min_arr[2])
    max_arr = [mx1, mx2, mx3]
    min_arr = [mn1, mn2, mn3]

print(max(max_arr), min(min_arr))