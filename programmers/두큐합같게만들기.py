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

# def solution(queue1, queue2):
#     from collections import deque
#     if sum(queue1 + queue2) % 2:
#         return -1

#     q = deque()
#     q.append((queue1, queue2, 0))
#     visited = [queue1]
#     while q:
#         q1, q2, cnt = q.popleft()

#         if sum(q1) == sum(q2):
#             return cnt

#         if len(q1) > 1:
#             q1_ , q2_ = q1[1:], q2 + [q1[0]]
#             if not q1_ in visited:
#                 q.append((q1_, q2_, cnt + 1))
#                 visited.append(q1_)

#         if len(q2) > 1:
#             q1_ , q2_ = q1 + [q2[0]], q2[1:]
#             if not q1_ in visited:
#                 q.append((q1_, q2_, cnt + 1))
#                 visited.append(q1_)
#     else:
#         return -1

print(solution(
    [3, 2, 7, 2],
    [4, 6, 5, 1]
))

"""
1 2 1 2, 1 10 1 2, 1 2 1 2
"""