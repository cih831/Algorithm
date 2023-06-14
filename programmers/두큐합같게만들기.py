def solution(queue1, queue2):
    arr = queue2 + queue1 + queue2
    arr_len = len(arr)
    arr_avg = sum(queue1 + queue2) // 2
    s, e, cnt = arr_len // 3, arr_len * 2 // 3, 0
    my_sum = sum(arr[s:e])
    while 0 <= s <= e < arr_len:
        if my_sum == arr_avg:
            return cnt
        elif my_sum > arr_avg:
            my_sum -= arr[s]
            s += 1
        else:
            my_sum += arr[e]
            e += 1
        cnt += 1
    else:
        return -1

print(solution(
    [3, 2, 7, 2],
    [4, 6, 5, 1]
))

"""
1 10 1 2, 1 2 1 2, 1 10 1 2
"""