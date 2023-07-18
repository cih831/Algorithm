def solution(expression):
    from itertools import permutations

    def operation(x, y, oper):
        if oper == "*":
            return x * y
        elif oper == "+":
            return x + y
        if oper == "-":
            return x - y

    def cal(lst, order, idx=0):
        if idx == 3:
            return lst[-1]
        tmp = []
        flag = 0
        for i in range(len(lst)):
            if flag:
                flag = 0
                tmp[-1] = operation(tmp[-1], lst[i], order[idx])
            elif lst[i] == order[idx]:
                flag = 1
            else:
                tmp.append(lst[i])
        return cal(tmp, order, idx + 1)

    answer = 0
    tmp = list(expression)
    arr = []
    permu = list(permutations("-*+", 3))

    for item in tmp:
        if item in "-*+":
            arr.append(item)
        else:
            item = int(item)
            if arr and not str(arr[-1]) in "-*+":
                arr[-1] = arr[-1] * 10 + item
            else:
                arr.append(item)

    for p in permu:
        res = abs(cal(arr, p))
        answer = max(answer, res)

    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
