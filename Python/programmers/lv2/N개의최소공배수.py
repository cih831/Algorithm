def solution(arr):
    answer = 1
    def div(num):
        lst = []
        d = 2
        while num > 1:
            if d > num ** 0.5:
                lst.append(num)
                break
            elif not num % d:
                num //= d
                lst.append(d)
            else:
                d += 1
        return lst
    for i in range(len(arr)):
        arr[i] = div(arr[i])
    for i in range(len(arr)):
        for _ in range(len(arr[i])):
            tmp = arr[i][0]
            answer *= tmp
            for lst in arr:
                if tmp in lst:
                    lst.remove(tmp)
    return answer

print(solution([2,6,8,14]))