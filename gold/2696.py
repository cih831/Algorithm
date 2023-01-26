import heapq

T = int(input())
for tc in range(1, T+1):
    M = int(input())
    print(M//2+1)
    arr = []
    for _ in range(M // 10 + 1):
        arr.extend(list(map(int, input().split())))
    cnt = 0

    small = [(2147483648, -2147483648)]
    big = [2147483648]

    for i in range(M):
        if not i % 2:
            if arr[i] < small[0][1]:
                heapq.heappush(small, (-arr[i], arr[i]))
                heapq.heappush(big, small[0][1])
            elif arr[i] > big[0]:
                heapq.heappush(big, arr[i])
                heapq.heappush(small, (-big[0], big[0]))
            elif small[0][1] <= arr[i] <= big[0]:
                heapq.heappush(big, arr[i])
                heapq.heappush(small, (-arr[i], arr[i]))
            print(big[0], end='')
            cnt += 1
            if cnt <= 9:
                print(end=' ')
            else:
                print()
                cnt = 0

        else:
            if arr[i] < small[0][1]:
                heapq.heappush(small, (-arr[i], arr[i]))
                heapq.heappop(big)
                heapq.heappush(big, heapq.heappop(small)[1])
            elif arr[i] > big[0]:
                heapq.heappush(big, arr[i])
                mid = heapq.heappop(big)
                heapq.heappop(small)
                heapq.heappush(small, (-mid, mid))

    print()